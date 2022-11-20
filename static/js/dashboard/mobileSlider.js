(function() {
  $(document).ready(function() {
    var walkthrough;
    walkthrough = {
      index: 0,
      nextScreen: function() {
        if (this.index < this.indexMax()) {
          this.index++;
          return this.updateScreen();
        }
      },
      prevScreen: function() {
        if (this.index > 0) {
          this.index--;
          return this.updateScreen();
        }
      },
      refreshScreen: function() {
          this.index = this.index + 2;
          return this.updateScreen();
      
      },
      back: function() {
        this.index = this.index - 2;
        return this.updateScreen();
      },
      updateScreen: function() {
        this.reset();
        this.goTo(this.index);
        return this.setBtns();
      },
      setBtns: function() {
        var $lastBtn, $nextBtn, $prevBtn, $refreshbtn, $backBtn;
        $nextBtn = $('.next-screen');
        $prevBtn = $('.prev-screen');
        $backBtn = $('.back');
        $refreshbtn = $('.refresh-screen');
    
        $lastBtn = $('.finish');
        $backBtn = $('.back');
        if (walkthrough.index === walkthrough.indexMax()) {
          $nextBtn.prop('disabled', true);
          $prevBtn.prop('disabled', false);
          return $lastBtn.addClass('active').prop('disabled', false);
        } else if (walkthrough.index === 0) {
          $nextBtn.prop('disabled', false);
          $prevBtn.prop('disabled', true);
          return $lastBtn.removeClass('active').prop('disabled', true);
        } else {
          $nextBtn.prop('disabled', false);
          $prevBtn.prop('disabled', false);
          return $lastBtn.removeClass('active').prop('disabled', true);
        }
      },
      goTo: function(index) {
        $('.screen').eq(index).addClass('active');
        return $('.dot').eq(index).addClass('active');
      },
      reset: function() {
        return $('.screen, .dot').removeClass('active');
      },
      indexMax: function() {
        return $('.screen').length - 1;
      },
      closeModal: function() {
        $('.walkthrough, .shade').removeClass('reveal');
        return setTimeout(((function(_this) {
          return function() {
            $('.walkthrough, .shade').removeClass('show');
            _this.index = 0;
            return _this.updateScreen();
          };
        })(this)), 200);
      },
      openModal: function() {
        $('.walkthrough, .shade').addClass('show');
        setTimeout(((function(_this) {
          return function() {
            return $('.walkthrough, .shade').addClass('reveal');
          };
        })(this)), 200);
        return this.updateScreen();
      }
    };
    $('.next-screen').click(function() {
      return walkthrough.nextScreen();
    });
    $('.prev-screen').click(function() {
      return walkthrough.prevScreen();
    });
    $('.close').click(function() {
      return walkthrough.closeModal();
    });
    $('.back').click(function() {
      return walkthrough.back();
    });
    $('.open-walkthrough').click(function() {
      return walkthrough.openModal();
    });
    $('.refresh-screen').click(function() {
      return walkthrough.refreshScreen();
    });
    walkthrough.openModal();
    return $(document).keydown(function(e) {
      switch (e.which) {
        case 37:
          walkthrough.prevScreen();
          break;
        case 38:
          walkthrough.openModal();
          break;
        case 39:
          walkthrough.nextScreen();
          break;
        case 40:
          walkthrough.closeModal();
          break;
        default:
          return;
      }
      e.preventDefault();
    });
  });

}).call(this);