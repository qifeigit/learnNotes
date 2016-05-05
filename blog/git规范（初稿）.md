#阿里文学前端团队 git 使用规范

团队开发中，遵循一个合理、清晰的Git使用流程，是非常重要的。为了前端团队研发的规范性，特制定此规范。


##目录
1.基本原则

2.建议流程


##基本原则

不到万不得已，不要跨分支提交

打开工程，拉取一次， 切换本地仓库分支，拉取一次

不要把系统临时文件，开发工具配置文件，项目配置文件，执行结果文件，编译过程文件，压缩优化文件，日志文件等等，反正是大部分开发者人一眼看不懂内容的文件，或者肯定会和队友冲突的文件，扔到git远程区上去，这样会制造百分百麻烦

拉取不成功，解决冲突，提交不成功，解决冲突，解决不了冲突，请联系队友

冲突解决后，别闲着，要提交，要提交，要提交！

推送前，一定确认还有没有文件没有提交，然后才是，看清楚推送的是谁到谁

除了部署服务器的pull的默认策略为rebase外，请默认pull的策略为merge



## 建议流程

### 第一步：新建分支

首先，每次开发新功能，都应该新建一个单独的分支

```bash
 获取主干最新代码

$ git checkout master
$ git pull

新建一个开发分支,以3.3.5.51为例

$ git checkout -b v3.3.5.51

```

### 第二步：提交分支commit

分支修改后，就可以提交commit了。

```bash
$ git add .
$ git status
$ git commit
```

git add 命令的all参数，表示保存所有变化（包括新建、修改和删除）。从Git 2.0开始，all是 git add 的默认参数，所以也可以用 git add . 代替。

git status 命令，用来查看发生变动的文件。

### 第三步：撰写提交信息

提交commit时，必须给出完整扼要的提交信息，下面是一个范本。

```bash
Present-tense summary under 50 characters

* More information about commit (under 72 characters).
* More information about commit (under 72 characters).

http://project.management-system.com/ticket/123
```

第一行是不超过50个字的提要，然后空一行，罗列出改动原因、主要变动、以及需要注意的问题。最后，提供对应的网址（比如Bug ticket）。

### 第四步：与主干同步

分支的开发过程中，要经常与远程当前分支保持同步。

```bash
$ git fetch origin
$ git rebase origin/v3.3.5.51
```

### 第五步：合并commit

分支开发完成后，很可能有一堆commit，但是合并到主干的时候，往往希望只有一个（或最多两三个）commit，这样不仅清晰，也容易管理。

那么，怎样才能将多个commit合并呢？这就要用到 git rebase 命令。

```bash
$ git rebase -i origin/v3.3.5.51
```

git rebase命令的i参数表示互动（interactive），这时git会打开一个互动界面，进行下一步操作。

下面采用[Tute Costa](https://robots.thoughtbot.com/git-interactive-rebase-squash-amend-rewriting-history)的例子，来解释怎么合并commit。

```bash
pick 07c5abd Introduce OpenPGP and teach basic usage
pick de9b1eb Fix PostChecker::Post#urls
pick 3e7ee36 Hey kids, stop all the highlighting
pick fa20af3 git interactive rebase, squash, amend

 Rebase 8db7e8b..fa20af3 onto 8db7e8b

 Commands:
  p, pick = use commit
  r, reword = use commit, but edit the commit message
  e, edit = use commit, but stop for amending
  s, squash = use commit, but meld into previous commit
  f, fixup = like "squash", but discard this commit's log message
  x, exec = run command (the rest of the line) using shell

 These lines can be re-ordered; they are executed from top to bottom.

 If you remove a line here THAT COMMIT WILL BE LOST.

 However, if you remove everything, the rebase will be aborted.

 Note that empty commits are commented out
```

上面的互动界面，先列出当前分支最新的4个commit（越下面越新）。每个commit前面有一个操作命令，默认是pick，表示该行commit被选中，要进行rebase操作。

4个commit的下面是一大堆注释，列出可以使用的命令。

> - pick：正常选中
> - reword：选中，并且修改提交信息；
> - edit：选中，rebase时会暂停，允许你修改这个commit（参考[这里](https://schacon.github.io/gitbook/4_interactive_rebasing.html)）
> - squash：选中，会将当前commit与上一个commit合并
> - fixup：与squash相同，但不会保存当前commit的提交信息
> - exec：执行其他shell命令

上面这6个命令当中，squash和fixup可以用来合并commit。先把需要合并的commit前面的动词，改成squash（或者s）。

```bash
pick 07c5abd Introduce OpenPGP and teach basic usage
s de9b1eb Fix PostChecker::Post#urls
s 3e7ee36 Hey kids, stop all the highlighting
pick fa20af3 git interactive rebase, squash, amend
```

这样一改，执行后，当前分支只会剩下两个commit。第二行和第三行的commit，都会合并到第一行的commit。提交信息会同时包含，这三个commit的提交信息。

```bash
 This is a combination of 3 commits.
 The first commit's message is:
Introduce OpenPGP and teach basic usage

 This is the 2nd commit message:
Fix PostChecker::Post#urls

 This is the 3rd commit message:
Hey kids, stop all the highlighting
```

如果将第三行的squash命令改成fixup命令。

```bash
pick 07c5abd Introduce OpenPGP and teach basic usage
s de9b1eb Fix PostChecker::Post#urls
f 3e7ee36 Hey kids, stop all the highlighting
pick fa20af3 git interactive rebase, squash, amend
```

运行结果相同，还是会生成两个commit，第二行和第三行的commit，都合并到第一行的commit。但是，新的提交信息里面，第三行commit的提交信息，会被注释掉。

```bash


 This is a combination of 3 commits.
 The first commit's message is:

Introduce OpenPGP and teach basic usage

 This is the 2nd commit message:

Fix PostChecker::Post#urls

 This is the 3rd commit message:

 Hey kids, stop all the highlighting
```

squash和fixup命令，还可以当作命令行参数使用，自动合并commit。

```bash
$ git commit --fixup <commit> 
$ git rebase -i --autosquash 
```

这个用法请参考[这篇文章](http://fle.github.io/git-tip-keep-your-branch-clean-with-fixup-and-autosquash.html)，这里就不解释了。

### 第六步：推送到远程仓库

合并commit后，就可以推送当前分支到远程仓库了。

```bash
$ git push --force origin v3.3.5.51
```

git push命令要加上force参数，因为rebase以后，分支历史改变了，跟远程分支不一定兼容，有可能要强行推送（参见[这里](http://willi.am/blog/2014/08/12/the-dark-side-of-the-force-push/)）。

