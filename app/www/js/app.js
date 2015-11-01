angular.module('starter', ['ionic', 'starter.controllers', 'starter.services'])
.constant('ApiEndpoint', {
  url: 'http://api.site.com'
})
.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})
.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

    .state('app', {
      url: '/app',
      abstract: true,
      templateUrl: 'templates/menu.html',
      controller: 'AppCtrl'
    })

    .state('app.users', {
      url: '/users',
      views: {
        'menuContent': {
          templateUrl: 'templates/users.html',
          controller: 'UsersCtrl'
        }
      }
    })

    .state('app.customers', {
      url: '/customers',
      views: {
        'menuContent': {
          templateUrl: 'templates/customers.html',
          controller: 'CustomersCtrl'
        }
      }
    })

    .state('app.orders', {
      url: '/orders',
      views: {
        'menuContent': {
          templateUrl: 'templates/orders.html',
          controller: 'OrdersCtrl'
        }
      }
    })

    .state('app.invoices', {
      url: '/invoices',
      views: {
        'menuContent': {
          templateUrl: 'templates/invoices.html',
          controller: 'InvoicesCtrl'
        }
      }
    })

    .state('app.products', {
      url: '/products',
      views: {
        'menuContent': {
          templateUrl: 'templates/products.html',
          controller: 'ProductsCtrl'
        }
      }
    })

    .state('app.user', {
      url: '/user/:id',
      views: {
        'menuContent': {
          templateUrl: 'templates/user.html',
          controller: 'UserCtrl'
        }
      }
    })

    .state('app.customer', {
      url: '/customer/:id',
      views: {
        'menuContent': {
          templateUrl: 'templates/customer.html',
          controller: 'CustomerCtrl'
        }
      }
    })

    .state('app.order', {
      url: '/order/:id',
      views: {
        'menuContent': {
          templateUrl: 'templates/order.html',
          controller: 'OrderCtrl'
        }
      }
    })

    .state('app.create_order', {
      url: '/create_order',
      views: {
        'menuContent': {
          templateUrl: 'templates/create_order.html',
          controller: 'AddSaleCtrl'
        }
      }
    })

    .state('app.invoice', {
      url: '/invoice/:id',
      views: {
        'menuContent': {
          templateUrl: 'templates/invoice.html',
          controller: 'InvoiceCtrl'
        }
      }
    })

    .state('app.product', {
      url: '/product/:id',
      views: {
        'menuContent': {
          templateUrl: 'templates/product.html',
          controller: 'ProductCtrl'
        }
      }
    })
    ;

  $urlRouterProvider.otherwise('/app/users');
});
