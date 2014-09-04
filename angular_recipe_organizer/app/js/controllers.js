/* Controllers */

angular.module('myApp.controllers', [])
    .controller('RecipeCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        // GET a list of all recipes
        Restangular.all('recipes').getList().then(function (recipes) {
            $scope.recipes = recipes;
        })
    }])


    .controller('AddRecipeCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        $scope.recipe = { ingredients: []};

        $scope.addRecipe = function() {
            Restangular.all('add-recipe/').customPOST($scope.recipe).then(function() {
                alert("Your recipe was successfully added!");
                $scope.recipe = { ingredients: []};
            }, function() {
                alert("There was a problem adding your recipe.");
            });
        };
    }])


    .controller('RecipeDetailsCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        

    }]);