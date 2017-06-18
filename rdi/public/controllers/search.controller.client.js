(function(){
    angular
        .module("rdiApp")
        .controller("searchController", searchController);
    function searchController(searchClientService){


        var vm = this;

        vm.search=search;

        function init() {


        }
        init();

        function search(text){
            var obj={
                queryStr:text
            };

           var promise= searchClientService.search(obj);
           promise.success(function (data) {
               console.log(data);
           })
               .error(function (err) {
                   console.log(err);
               })

        }



    }
})();



