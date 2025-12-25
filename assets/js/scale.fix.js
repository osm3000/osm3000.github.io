(function() {
  var metas = document.getElementsByTagName('meta');
  var i;

  // iPhone scale fix
  if (navigator.userAgent.match(/iPhone/i)) {
    for (i = 0; i < metas.length; i++) {
      if (metas[i].name === 'viewport') {
        metas[i].content = 'initial-scale=1.0,maximum-scale=1.0';
      }
    }
    document.addEventListener('gesturestart', function() {
      for (i = 0; i < metas.length; i++) {
        if (metas[i].name === 'viewport') {
          metas[i].content = 'initial-scale=1.0,minimum-scale=0.25,maximum-scale=1.6';
        }
      }
    }, false);
  }
})();
