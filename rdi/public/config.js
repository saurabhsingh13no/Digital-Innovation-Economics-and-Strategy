(function(){
    angular
        .module("rdiApp")
        .config(configuration);

    function configuration($routeProvider, $httpProvider) {

        $httpProvider.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
        $httpProvider.defaults.headers.put['Content-Type'] = 'application/json;charset=utf-8';

        $routeProvider
            .when("/",{
                templateUrl: "./views/search.view.client.html",
                controller:'searchController',
                controllerAs:'model'

            })
            .when("default",{
                templateUrl: "./views/search.view.client.html",
                controller:'searchController',
                controllerAs:'model'
            });




    }})();