angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);
    $scope.closeLogin();
  };
})

.controller('UsersCtrl', function($scope, Users) {
  var URL = "http://localhost:8080/";
  var resource = "users";
  Users.get(URL+resource)
    .then(function(data) {
      $scope.users = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET Users error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})

.controller('UserCtrl', function($scope, Users, $stateParams) {
  var URL = "http://localhost:8080/";
  var resource = "user/"+$stateParams.id;
  Users.get(URL+resource)
    .then(function(data) {
      $scope.user = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET User error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})

.controller('CustomersCtrl', function($scope, Customers) {
  var URL = "http://localhost:8080/";
  var resource = "customers";
  Customers.get(URL+resource)
    .then(function(data) {
      $scope.customers = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET Users error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})

.controller('CustomerCtrl', function($scope, Customers, $stateParams) {
  var URL = "http://localhost:8080/";
  var resource = "customer/"+$stateParams.id;
  Customers.get(URL+resource)
    .then(function(data) {
      $scope.customer = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET Customer error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})

.controller('OrdersCtrl', function($scope, Orders) {
  var URL = "http://localhost:8080/";
  var resource = "orders";
  Orders.get(URL+resource)
    .then(function(data) {
      $scope.orders = data;
      //console.log(data);
    })
    .catch(function(data, status) {
      //console.error('GET Orders error', response.status, response.data);
    })
    .finally(function() {
      //console.log("finally finished GET");
    });
})

.controller('OrderCtrl', function($scope, Orders, $stateParams) {
  var URL = "http://localhost:8080/";
  var resource = "order/"+$stateParams.id;
  Orders.get(URL+resource)
    .then(function(data) {
      $scope.order = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET Order error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})

.controller('InvoicesCtrl', function($scope, Orders) {
  var URL = "http://localhost:8080/";
  var resource = "invoices";
  Orders.get(URL+resource)
    .then(function(data) {
      $scope.invoices = data;
      //console.log(data);
    })
    .catch(function(data, status) {
      //console.error('GET Orders error', response.status, response.data);
    })
    .finally(function() {
      //console.log("finally finished GET");
    });
})

.controller('InvoiceCtrl', function($scope, Invoices, $stateParams) {
  var URL = "http://localhost:8080/";
  var resource = "invoice/"+$stateParams.id;
  Invoices.get(URL+resource)
    .then(function(data) {
      $scope.invoice = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET Invoice error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})

.controller('ProductsCtrl', function($scope, Products) {
  var URL = "http://localhost:8080/";
  var resource = "products";
  Products.get(URL+resource)
    .then(function(data) {
      $scope.products = data;
      //console.log(data);
    })
    .catch(function(data, status) {
      //console.error('GET Products error', response.status, response.data);
    })
    .finally(function() {
      //console.log("finally finished GET");
    });
})

.controller('ProductCtrl', function($scope, Products, $stateParams) {
  var URL = "http://localhost:8080/";
  var resource = "product/"+$stateParams.id;
  Products.get(URL+resource)
    .then(function(data) {
      $scope.product = data;
      console.log(data);
    })
    .catch(function(data, status) {
      console.error('GET Product error', response.status, response.data);
    })
    .finally(function() {
      console.log("finally finished GET");
    });
})
;
