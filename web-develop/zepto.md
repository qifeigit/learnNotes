###[zepto事件对象学习](http://www.cnblogs.com/yexiaochai/p/3448500.html)


###判断一个对象是否是函数
可参考'javascript高级程序设计'

```javascript
  $.each = function(elements, callback){
    var i, key
    if (likeArray(elements)) {
      for (i = 0; i < elements.length; i++)
        if (callback.call(elements[i], i, elements[i]) === false) return elements
    } else {
      for (key in elements)
        if (callback.call(elements[key], key, elements[key]) === false) return elements
    }
    return elements
}

``` 
上述代码中，通过'likeArray'来分开进行处理，为什么要这么做
