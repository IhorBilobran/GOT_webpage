app.factory('Post', function($resource){
  return $resource('/accounts/api/posts/?format=json');
});

app.controller('profileCtrl', function($scope, Post){
  $scope.posts = Post.query();

  $scope.addPost = function(){
    var sendData = {title: $scope.titleInput, text: $scope.textInput};
    Post.save(sendData);
    $scope.titleInput = '';
    $scope.textInput = '';
    $scope.posts = Post.query();

  };
});
