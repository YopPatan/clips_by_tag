angular.module('copaApp', [])
    .controller('VideosCtrl', function($scope, $http, $timeout) {
        $scope.isVideo = false;
        $scope.isLista = true;

        $scope.loadData = function() {
            if ($scope.isLista) {
                $http.get('../services/data/data_fiesta.json').then(function(response) {
                    //$scope.isLista = true;
                    console.log(response);
                    $scope.video_list = response.data;
                    //$timeout($scope.loadData, 10000);
                });
            }
            $timeout($scope.loadData, 60000);
        }

        $scope.showVideo = function(video) {
            //console.log('entroooo');
            $scope.currentVideo = video;
            $scope.isLista = false;
            $scope.isVideo = true;


            var param = {
                url: video.video_hls,
                imagen: video.thumbnail,
                autoPlay: 1
            }
            //$timeout($scope.loadMedia, 5000);
            $timeout(play.bind(null, 'player1',param), 500);
        }

        $scope.hideVideo = function() {
            $scope.isVideo = false;
            $scope.isLista = true;
        }

        $scope.loadData();

    });
