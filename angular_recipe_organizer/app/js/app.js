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
    config(['$routeProvider', 'RestangularProvider', function ($routeProvider, RestangularProvider) {
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

            .otherwise({
                redirectTo: '/recipes'
            });

        RestangularProvider.setBaseUrl('http://localhost:8001');
    }]);


