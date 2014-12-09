'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
        'ngRoute',
        'myApp.filters',
        'myApp.services',
        'myApp.directives',
        'myApp.controllers',
        'restangular'


    ]).
    config(['$routeProvider', '$sceDelegateProvider', 'RestangularProvider', function ($routeProvider, $sceDelegateProvider, RestangularProvider) {
        $routeProvider
            .when('/recipes', {
                templateUrl: 'partials/recipes.html',
                controller: 'RecipeCtrl',
                title: 'Recipe List'
            })

            .when('/add-recipe', {
                templateUrl: 'partials/add-recipe.html',
                controller: 'AddRecipeCtrl',
                title: 'Add a Recipe'
            })

            .when('/recipes/:id', {
                templateUrl: 'partials/recipe-detail.html',
                controller: 'RecipeDetailsCtrl',
                title: 'Recipe Details'
            })

            .when('/edit-recipe/:recipeId', {
                templateUrl: 'partials/edit-recipe.html',
                controller: 'EditRecipeCtrl',
                title: 'Edit Recipe'
            })

            .otherwise({
                redirectTo: '/recipes'
            });

        $sceDelegateProvider.resourceUrlWhitelist(['self', new RegExp('^(http[s]?):\/\/(w{3}.)?youtube.com/.+$')]);

        RestangularProvider.setBaseUrl('http://localhost:8001');

    }])


