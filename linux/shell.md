[linux命令的](http://man.linuxde.net/)

查看一级目录的大小
du -h --max-depth=1 | sort -n


查看最近修改的文件
find ./mnt  -mmin 180
