angular.module('copaApp', [])
    .controller('VideosCtrl', function($scope, $http, $timeout) {
        $scope.isVideo = false;
        $scope.isLista = true;

        $scope.nombre_json = document.getElementById("nombre_json").value;
        $scope.partido_equipos = document.getElementById("partido_equipos").value;
        $scope.partido_fecha = document.getElementById("partido_fecha").value;
        //console.log(document.getElementById("nombre_json").value);

        $scope.loadData = function() {
            if ($scope.isLista) {
                $http.get('../services/data/' + $scope.nombre_json).then(function(response) {
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
            $timeout(play.bind(null, 'videoMS', param), 500);
        }

        $scope.hideVideo = function() {
            $scope.isVideo = false;
            $scope.isLista = true;
        }

        $scope.loadData();

    });
