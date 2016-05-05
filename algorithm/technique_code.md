
###将数组打乱
        var result = ["哈哈", "大大", '爽肤水'];
        var text = "哈大爽肤水大哈";
将result 拼接成 text ，并将其顺序打乱。

如果不考虑打乱,这个问题很easy.

```javascript
//use javascript
                result = result.join('').split('');
            // if(result.length<25){
            //     result +='的发生';
            // }
            function random(min, max) {
                if (max == null) {
                    max = min;
                    min = 0;
                }
                return min + Math.floor(Math.random() * (max - min + 1));
            };
             function shuffle(obj) {
                var rand;
                var index = 0;
                var shuffled = [];
                for(var key in obj) {
                    console.log(key);
                    rand =random(index++);
                    shuffled[index - 1] = shuffled[rand];
                    shuffled[rand] = obj[key];
                }
                console.log(shuffled);
                return shuffled;
            };
            console.log(result);
```