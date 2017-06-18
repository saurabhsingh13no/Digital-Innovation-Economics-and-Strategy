(function (){
    angular
        .module("rdiApp")
        .factory("searchClientService",searchClientService);

    function searchClientService ($http) {


        var api = {
            search:search
        };


        return api;


        function search (textObj) {
            return $http.put('/api/search/', textObj);

        }

    }
})();