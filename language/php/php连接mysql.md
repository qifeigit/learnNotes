步骤
1.接收前端传来的数据（格式为json）
2.将其转化为php形式（对象或数组）
3.将php化的数据写入数据库中
4.向php中返回值
```php
        //创建简单的库
        $dbc = mysqli_connect('localhost','root','usbw','new_db');

        //此处是想删除一个表 
        $delete = 'DROP TABLE IF EXISTS `hx_group`'
        // mysqli_query($dbc,$delete);
8        $dbc->query("DROP TABLE 'hx_group'");
```

会报如下错误
Parse error: syntax error, unexpected T_VARIABLE in D:\appserv\www\analysis\mysql.php on line 8