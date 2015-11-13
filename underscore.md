
###在最外层有这样的写法
```javascript
    (function(){
        ...
    }).call(this);
```
###??上面的写法和下面的写法有何区别？


```javascript
    (function(){
        ...
    })(this);
```
注：'underscore'可用于浏览器和非浏览器环境

```javascript
 // Establish the root object, `window` in the browser, or `exports` on the server.
  var root = this;
  
  ...

  // Export the Underscore object for **Node.js**, with
  // backwards-compatibility for the old `require()` API. If we're in
  // the browser, add `_` as a global object via a string identifier,
  // for Closure Compiler "advanced" mode.
  if (typeof exports !== 'undefined') {
    if (typeof module !== 'undefined' && module.exports) {
      exports = module.exports = _;
    }
    exports._ = _;
  } else {
    root._ = _;
  }

```


