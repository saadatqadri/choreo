app = angular.module 'choreo.app.basic', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.changes = []
    $http.get('/api/changes').then (result) ->
        angular.forEach result.data, (item) ->
            $scope.changes.push item
]
