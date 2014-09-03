'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('MyCtrl1', ['$scope', 'Restangular', function ($scope, Restangular) {
        Restangular.all('recipes').getList().then(function(recipes){
            $scope.recipes = recipes;
        });
    }])