// app.factory('AuthenticationService', AuthenticationService);
// app.factory('FlashService', FlashService);

// AuthenticationService.$inject = ['$http', '$cookies', '$rootScope', '$timeout', 'UserService'];

// function AuthenticationService($http, $cookies, $rootScope, $timeout, UserService) {
// 	var service = {};

// 	service.Login = Login;
// 	service.SetCredentials = SetCredentials;
// 	service.ClearCredentials = ClearCredentials;

// 	return service;

// 	function Login(username, password, callback) {
// 		console.log('111111111111')
// 		$timeout(function () {
// 			var response;
// 			UserService.GetByUsername(username)
// 			.then(function (user) {
// 				if (user !== null && user.password === password) {
// 					response = { success: true };
// 				} else {
// 					response = { success: false, message: 'Username or password is incorrect' };
// 				}
// 				callback(response);
// 			});
// 		}, 1000);
// 	}

// 	function SetCredentials(username, password) {
// 		console.log('88888888888')
// 		var authdata = Base64.encode(username + ':' + password);

// 		$rootScope.globals = {
// 			currentUser: {
// 				username: username,
// 				authdata: authdata
// 			}
// 		};

// 	    // set default auth header for http requests
// 	    $http.defaults.headers.common['Authorization'] = 'Basic ' + authdata;

// 	    // store user details in globals cookie that keeps user logged in for 1 week (or until they logout)
// 	    var cookieExp = new Date();
// 	    cookieExp.setDate(cookieExp.getDate() + 7);
// 	    $cookies.putObject('globals', $rootScope.globals, { expires: cookieExp });
// 	}

// 	function ClearCredentials() {
// 		$rootScope.globals = {};
// 		$cookies.remove('globals');
// 		$http.defaults.headers.common.Authorization = 'Basic';
// 	}
// }


// FlashService.$inject = ['$rootScope'];

// function FlashService($rootScope) {
// 	console.log('aaaaaaaaaaaa')
// 	var service = {};

// 	service.Success = Success;
// 	service.Error = Error;

// 	initService();

// 	return service;

// 	function initService() {
// 		console.log('bbbbbbbbb')
// 		$rootScope.$on('$locationChangeStart', function () {
// 			clearFlashMessage();
// 		});

// 		function clearFlashMessage() {
// 			var flash = $rootScope.flash;
// 			if (flash) {
// 				if (!flash.keepAfterLocationChange) {
// 					delete $rootScope.flash;
// 				} else {
//                     // only keep for a single location change
//                     flash.keepAfterLocationChange = false;
//                 }
//             }
//         }
//     }

//     function Success(message, keepAfterLocationChange) {
//     	console.log('cccccccc')
//     	$rootScope.flash = {
//     		message: message,
//     		type: 'success', 
//     		keepAfterLocationChange: keepAfterLocationChange
//     	};
//     }

//     function Error(message, keepAfterLocationChange) {
//     	console.log('dddddddddddd')
//     	$rootScope.flash = {
//     		message: message,
//     		type: 'error',
//     		keepAfterLocationChange: keepAfterLocationChange
//     	};
//     }
// }	