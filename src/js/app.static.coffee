app = angular.module 'choreo.app.static', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
	$scope.changes = [
		title: 'Remove LEMSi1A'
		description: 'Reboot on demand'
	,
		title: 'Add new ORMS Server'
		description: 'New changes required'
	]
]
