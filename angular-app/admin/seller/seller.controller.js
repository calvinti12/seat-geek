(function(angular) {
  'use strict';

  angular
    .module('app.controllers')
    .controller('SellerCtrl', sellerCtrl);

  sellerCtrl.$inject = [
    'SellerModel',
  ];

  function sellerCtrl(Seller) {
    var seller = this;
    seller.submit = Seller.submit;
    seller.uploader = Seller.uploader;
    seller.model = Seller;

    function activate(){
      Seller.listing(active_user.key);
    }

    activate();

  }
})(window.angular);
