[linux命令的](http://man.linuxde.net/)

查看一级目录的大小
du -h --max-depth=1 | sort -n


查看最近修改的文件
find ./mnt  -mmin 180

改变文件用户及组
chown user:group xx.txt


强制执行logrotate

logrotate --force /etc/logrotate.d/tomcat
https://jin-yang.github.io/post/logrotate-usage.html

/var/log/catalina.out {
        daily
       rotate 10
       size +50k
       missingok
        copytruncate
   }
   
   
   free命令详解 https://www.cnblogs.com/coldplayerest/archive/2010/02/20/1669949.html          
   

scp限速
http://blog.mreald.com/108
