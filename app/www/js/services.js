angular.module('starter.services', [])

.factory('Users', function($http, $q) {
  return {
    get: function() {
      var deferred = $q.defer();
      $http.get.apply(null, arguments)
        .success(deferred.resolve)
        .error(deferred.resolve);
      return deferred.promise;
    }
  }
})

.factory('Customers', function($http, $q) {
  return {
    get: function() {
      var deferred = $q.defer();
      $http.get.apply(null, arguments)
        .success(deferred.resolve)
        .error(deferred.resolve);
      return deferred.promise;
    }
  }
})

.factory('Orders', function($http, $q) {
  return {
    get: function() {
      var deferred = $q.defer();
      $http.get.apply(null, arguments)
        .success(deferred.resolve)
        .error(deferred.resolve);
      return deferred.promise;
    }
  }
})

.factory(
  "transformRequestAsFormPost",
  function() {
      function transformRequest( data, getHeaders ) {
          var headers = getHeaders();
          headers[ "Content-type" ] = "application/x-www-form-urlencoded; charset=utf-8";
          return( serializeData( data ) );
      }
      return( transformRequest );

      function serializeData( data ) {
          if ( ! angular.isObject( data ) ) {
              return( ( data == null ) ? "" : data.toString() );
          }
          var buffer = [];
          for ( var name in data ) {
              if ( ! data.hasOwnProperty( name ) ) {
                  continue;
              }
              var value = data[ name ];
              buffer.push(
                  encodeURIComponent( name ) +
                  "=" +
                  encodeURIComponent( ( value == null ) ? "" : value )
              );
          }
          var source = buffer
              .join( "&" )
              .replace( /%20/g, "+" )
          ;
          return( source );
      }
  })



.factory('Invoices', function($http, $q) {
  return {
    get: function() {
      var deferred = $q.defer();
      $http.get.apply(null, arguments)
        .success(deferred.resolve)
        .error(deferred.resolve);
      return deferred.promise;
    }
  }
})

.factory('Products', function($http, $q) {
  return {
    get: function() {
      var deferred = $q.defer();
      $http.get.apply(null, arguments)
        .success(deferred.resolve)
        .error(deferred.resolve);
      return deferred.promise;
    }
  }
})
;
