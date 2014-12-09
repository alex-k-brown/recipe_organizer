/* Controllers */

angular.module('myApp.controllers', [])
    .controller('RecipeCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        // GET a list of all recipes
        Restangular.all('recipes/').getList().then(function (recipes) {
            $scope.recipes = recipes;
            $scope.orderProp = 'rating';
            $scope.quantity = 5;
        })
    }])

    .controller('AddRecipeCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        $scope.addIngredient = function() {
            $scope.createNewIngredient = true;
        };

        $scope.saveIngredient = function(name) {
            //ensure no duplicates

            if(ingredientExists(name)) {
                $scope.newIngredient.$error = true

                return;
            }

            $scope.createNewIngredient = false;
            var obj={
                name:name
            };
            Restangular.all("ingredients/").customPOST(obj).then(function(ingredient) {
                $scope.ingredients.push(ingredient);
                $scope.newIngredient = {};
            });
        };

        $scope.cancelIngredient = function() {
            $scope.newIngredient = {}
            $scope.newIngredient = false;

        };

        var ingredientExists = function(name) {
          for (var i=0; i<$scope.ingredients.length; i++) {
              if (name.toLowerCase()=== $scope.ingredients[i].name.toLowerCase()) {
                  return true;
              }
          }
        };

        Restangular.all("ingredients/").getList().then(function(ingredients){

           $scope.ingredients=ingredients
        });
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


    .controller('RecipeDetailsCtrl', ['$scope', '$routeParams', 'Restangular', function ($scope, $routeParams, Restangular) {
        $scope.editing = false;
        var id = $routeParams.id;
        Restangular.one('recipes/', id).get().then(function(recipe){
            $scope.recipe = recipe
        });
        $scope.saveRecipe = function(){
            $scope.recipe.put();
            $scope.editing = false
        };
        $scope.deleteRecipe = function(){
            if(confirm("Are you sure you want to delete this recipe?")){
                $scope.recipe.remove();
                window.location = "#/recipes"

            }
        }
}]);
/*
    .controller('EditRecipeCtrl', function($scope, Restangular, $routeParams, $location) {
    $scope.recipeId = $routeParams.recipeId;

    Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
        $scope.recipe = data;
    });


    $scope.updateRecipe = function() {
        Restangular.one('recipes', $scope.recipeId).customPUT($scope.recipe).then(function (data) {
            $scope.status = "The recipe was successfully edited!";
            $scope.recipe = data;
            $location.path('/recipes');
        }, function() {
            $scope.status = "The recipe couldn't be saved";
        }
    )};
});*/
