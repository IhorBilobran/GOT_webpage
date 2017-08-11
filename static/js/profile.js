function findElement(arr, propName, propValue) {
  for (var i=0; i < arr.length; i++)
    if (arr[i][propName] == propValue)
      return arr[i];

  // will return undefined if not found; you could return a default instead
}


app.factory('Post', function($resource){
  return $resource('/accounts/api/posts/:id', {id: '@id'},{
      save:{
        method: 'POST',
        params: {id: '.json'}
      },
      delete_post:{
        method: 'DELETE',
      }
  });
});

app.controller('profileCtrl', function($scope, $http, Post){
  $scope.posts = Post.query();

  $scope.addPost = function(){
    var sendData = {title: $scope.titleInput, text: $scope.textInput};
    Post.save(sendData);
    $scope.titleInput = '';
    $scope.textInput = '';
    $scope.posts = Post.query();
  };

  $scope.removePost = function(id) {
    $http.delete('/accounts/api/posts/'+id);
    $scope.posts = Post.query();

  };

  $scope.editPost = function(id) {
    var post = findElement($scope.posts, 'id', id);
    var title = post.title;
    var text  = post.text;
    var id = post.id;
    $scope.titleInput = title;
    $scope.textInput = text;
    $scope.postIdInput = id
    document.getElementById('post').style.display = "none";
    document.getElementById('update').style.display = "inline";

  };

  $scope.updatePost = function(){
    var sendData = {title: $scope.titleInput, text: $scope.textInput};
    var id = $scope.postIdInput;
    $scope.titleInput = '';
    $scope.textInput = '';
    $scope.postIdInput = '';
    $http.put('/accounts/api/posts/'+id+'/', sendData);
    $scope.posts = Post.query();
    document.getElementById('update').style.display = "none";
    document.getElementById('post').style.display = "inline";
  };
});
