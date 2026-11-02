$(function() {
  var $torch = $('.torch');

  function updateTorch(x, y) {
    $torch.css({
      'top': y + 'px',
      'left': x + 'px',
      'transform': 'translate(-50%, -50%)'
    });
  }

  $(document).on('mousemove', function (e) {
    updateTorch(e.clientX, e.clientY);
  });

  $(document).on('touchmove', function (e) {
    if (e.originalEvent.touches && e.originalEvent.touches.length > 0) {
      var touch = e.originalEvent.touches[0];
      updateTorch(touch.clientX, touch.clientY);
    }
  });
});
