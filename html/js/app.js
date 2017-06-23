var app = angular.module('copaApp', []);

app.controller('VideosCtrl', function($scope, $http, $timeout, $location, $filter) {

    //console.log($location.absUrl());
    var url = new URL($location.absUrl());
    var video_id = url.searchParams.get("id");

    $scope.nombre_json = document.getElementById("nombre_json").value;
    $scope.partido_equipos = document.getElementById("partido_equipos").value;
    $scope.partido_fecha = document.getElementById("partido_fecha").value;
    //console.log(document.getElementById("nombre_json").value);

    $scope.loadData = function() {
        if ($scope.isLista) {
            $http.get('http://localhost/clips_by_tag/services/data/' + $scope.nombre_json).then(function(response) {
                //$scope.isLista = true;
                //console.log(response);
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

        ga('send', 'event', 'copa_confederaciones','play: ' + video.title, window.location.href);

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

    if (video_id != null) {
        $scope.isVideo = true;
        $scope.isLista = false;
        $scope.isShared = true;

        $http.get('http://localhost/clips_by_tag/services/data/' + $scope.nombre_json).then(function(response) {
            $scope.video_list = response.data;
            var videos = $filter('filter')(response.data, {'id': video_id}, true);
            if (videos.length > 0) {
                $scope.showVideo(videos[0]);
            }
            else {
                $scope.isVideo = false;
                $scope.isLista = true;
                $scope.isShared = false;
                $scope.loadData();
            }

            //console.log($filter('filter')(response.data, {'id': '5948113940992704b7163e00'}, true));
            //console.log(response.data);
        });
    }
    else {
        $scope.isVideo = false;
        $scope.isLista = true;
        $scope.isShared = false;
        $scope.loadData();
    }

});
