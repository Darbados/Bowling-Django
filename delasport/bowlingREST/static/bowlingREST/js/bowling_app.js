let values = [0,1,2,3,4,5,6,7,8,9,10];
let game_id = Number($('#game_id').val());
let current_frame = Number($('#frame_counter').val());
let current_roll = Number($("#counter_rolls").val());
let total = 0;
let button_click_counter = 0;

function possibleValue2(value1){
  switch(value1){
    case 1:
      values = [0,2,3,4,5,6,7,8,9];
      break;
    case 2:
      values = [0,1,3,4,5,6,7,8];
      break;
    case 3:
      values = [0,1,2,4,5,6,7];
      break;
    case 4:
      values = [0,1,2,3,5,6];
      break;
    case 5:
      values = [0,1,2,3,4,5];
      break;
    case 6:
      values = [0,1,2,3,4];
      break;
    case 7:
      values = [0,1,2,3];
      break;
    case 8:
      values = [0,1,2];
      break;
    case 9:
      values = [0,1];
      break;
    case 10:
      values = [0];
      break;
    case 0:
      values = values;
      break;
    default:
      break;
  }
}


if (current_frame < 19) {
  $("#roll1").on('click', function(){
    if ($(".table").find('tr').find('td').eq(0).find('.place').val() != 'X'){
      $(this).addClass('hidden');
      $("#roll2").removeClass('hidden');
    } else {
      $(this).addClass('hidden');
      $("input[type=submit]").removeClass('hidden');
    }
  });
  $("#roll2").on('click', function(){
      $(this).addClass('hidden');
      $("input[type=submit]").removeClass('hidden');
  });
  $("input[type=submit]").click(function(e){
    //e.preventDefault();
    $(this).addClass('hidden');
    if ((current_frame+1) < 19){
      $("#roll1").removeClass('hidden');
    }
  });
} else {
    $('.table').find('tr').find('td:last').removeClass('hidden');

    $("#roll1").on('click', function(){
      console.log($(".table").find('tr').find('td').eq(0).find('.place').val());
      if ($(".table").find('tr').find('td').eq(0).find('.place').val() != 'X'){
        $(this).addClass('hidden');
        $("#roll2").removeClass('hidden');
      } else {
        $(this).addClass('hidden');
        $("#roll3").removeClass('hidden');
      }
    });
    $("#roll2").on('click', function(){
        $(this).addClass('hidden');
        if ($(".table").find('tr').find('td').eq(1).find('.place').val() != '/') $("input[type=submit]").removeClass('hidden');
        else $("#roll3").removeClass('hidden');
    });
    $("#roll3").on('click', function(){
        $(this).addClass('hidden');
        $("input[type=submit]").removeClass('hidden');
    });

    $("input[type=submit]").click(function(e){
        //e.preventDefault();
        $(this).addClass('hidden');
        $("#to_total_score").removeClass('hidden');
      });
  }


function re_calculate(frames_score){
  let temp = frames_score;

  for (let i=0; i<temp.length; i++){
    if (temp[i].strike){
      try {
        temp[i+1].total;
        if (temp[i+1].strike){
          try {
            temp[i+2].total;
            temp[i].total = temp[i].total + temp[i+1].total + temp[i+2].total;
          } catch (e){
            temp[i].total = temp[i].total + temp[i+1].total
          }
        }
      } catch (e){
        temp[i].total = temp[i].total
      }
    } else if (temp[i].spare){
      try {
        temp[i+1].roll1;
        temp[i].total = temp[i].total + temp[i+1].roll1;
      } catch (e){
        temp[i].total = temp[i].total
      }
    } else {
      temp[i].total = temp[i].total;
    }
  }
  return temp;
}


let bowlingApp = angular.module('bowlingApp', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken'
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
});

bowlingApp.controller('BowlingController', function($scope, $http){
  $scope.game = {};
  $scope.rolls = {};
  $scope.rollsFrame = {};
  $scope.simpleCounter = 1;
  $scope.displayResults = [];


  /*
  * The get request to the API to handle the page refreshing
  */
  $scope.initFunc = function(){
    $scope.frames = [];

    $http.get('/bowlingREST/api/' + game_id + '/').then(function(response){
      $scope.game = response.data
      for (let i=1; i<response.data.counterFrames; i++){
        $scope.rolls['roll' + i] = $scope.game['roll' + i];
      }

      for (let i=1; i<=response.data.counterFrames-2; i+=2){
        if (i < 19) $scope.frames.push({roll1: response.data['roll'+i], roll2: response.data['roll'+(i+1)]});
        else $scope.frames.push({roll1: response.data['roll'+i], roll2: response.data['roll'+(i+1)], roll3: response.data['roll'+(i+2)]});
      }


      /*
      * Reformating the frames for displaying
      */
      $scope.frames.forEach(function(el, index){
        el.frame = 'Frame ' + ++index;
        if (!el.roll3){
          if (el.roll1 == 10){
            el.roll1 = 'X';
            el.roll2 = '-';
            el.total = 10;
            el.strike = true;

          }
          else if ((el.roll1+el.roll2) == 10 && el.roll1 != 10) {
            el.roll2 = '/';
            el.total = 10;
            el.spare = true;
          }
          else {
            el.roll1 = (el.roll1 == 0 ? '-' : el.roll1);
            el.roll2 = (el.roll2 == 0 ? '-' : el.roll2);
            el.total = (el.roll1 == '-' ? 0 : el.roll1)+(el.roll2 == '-' ? 0 : el.roll2);
            el.strike = false;
            el.spare = false;
          }
        } else {
          if (el.roll1 == 10){
            el.roll1 = 'X';
            el.roll2 = '-';
            if (el.roll3 == 10){
              el.roll3 = '/';
            } else {
              el.roll3 = el.roll3
            }
            el.total = 20;
          } else if ((el.roll1+el.roll2) == 10){
            el.roll1 = el.roll1;
            el.roll2 = '/';
            if (el.roll3 == 10){
              el.roll3 = '/';
              el.total = 20;
            } else {
              el.roll3 = el.roll3;
              el.total = 10+el.roll3;
            }
          } else {
            el.total = el.roll1+el.roll2;
          }
        }
      });

      $scope.frames = re_calculate($scope.frames);
    });
  }

  setTimeout(function(){
    $scope.initFunc();
  },100);

  /*
  * The add_roll method which works on client side to display the results from the made rolls

  $scope.add_roll = function(){
    $scope.frames.push($scope.rollsFrame);


    $scope.frames.forEach(function(el, index){
      el.frame = 'Frame ' + ++index;
      if (!el.roll3){
        if (el.roll1 == 10){
          el.roll1 = 'X';
          el.roll2 = '-';
          el.total = 10;
          el.strike = true;

        }
        else if ((el.roll1+el.roll2) == 10 && el.roll1 != 10) {
          el.roll2 = '/';
          el.total = 10;
          el.spare = true;
        }
        else {
          el.roll1 = (el.roll1 == 0 ? '-' : el.roll1);
          el.roll2 = (el.roll2 == 0 ? '-' : el.roll2);
          el.total = (el.roll1 == '-' ? 0 : el.roll1)+(el.roll2 == '-' ? 0 : el.roll2);
          el.strike = false;
          el.spare = false;
        }
      } else {
        if (el.roll1 == 10){
          el.roll1 = 'X';
          el.roll2 = '-';
          if (el.roll3 == 10){
            el.roll3 = '/';
          } else {
            el.roll3 = el.roll3
          }
        } else if ((el.roll1+el.roll2) == 10){
          el.roll1 = el.roll1;
          el.roll2 = '/';
          if (el.roll3 == 10){
            el.roll3 = '/';
          } else {
            el.roll3 = el.roll3
          }
        }
      }
    });

    $scope.frames = re_calculate($scope.frames);
    console.log($scope.frames);

    $scope.rolls = {};
    $scope.rollsFrame = {};
    $scope.simpleCounter = 1;



  }*/


  /*
  * The save_roll method which makes the PUT request into the API
  */
 $scope.add_roll = function(){
   for (let i=1; i<$scope.game.counterFrames; i++){
     $scope.game['roll' + i] = $scope.rolls['roll' + i];
   }
   $http.put('/bowlingREST/api/' + game_id + '/', $scope.game);

   setTimeout(function() {
     $scope.rolls = {};
     $scope.rollsFrame = {};
     $scope.simpleCounter = 1;

     if ($scope.game.counterFrames < 19){
      $scope.initFunc();
    } else window.location.reload(false);

  },100);
 }

 /*
 * The makeRoll method which gives us the result from each row.
 */
  $scope.makeRoll = function(){
    let random_value = values[Math.floor(Math.random()*values.length)];
    $scope.rolls['roll' + $scope.game.counterFrames] = random_value;
    if ($scope.game.counterFrames < 19){
      if (random_value == 10){
        $scope.rollsFrame['roll' + $scope.simpleCounter] = 'X';
      } else if (random_value == 0){
        $scope.rollsFrame['roll' + $scope.simpleCounter] = '-';
      } else if (($scope.rollsFrame['roll' + ($scope.simpleCounter-1)] + random_value) == 10){
        $scope.rollsFrame['roll' + $scope.simpleCounter] = '/';
      } else {
        $scope.rollsFrame['roll' + $scope.simpleCounter] = random_value;
      }
    } else {
      if (random_value == 10){
        $scope.rollsFrame['roll' + $scope.simpleCounter] = 'X';
        $scope.rollsFrame['roll' + ++$scope.simpleCounter] = '-';
      } else if (random_value == 0){
        $scope.rollsFrame['roll' + $scope.simpleCounter] = '-';
      } else if (($scope.rollsFrame['roll' + ($scope.simpleCounter-1)] + random_value) == 10){
        $scope.rollsFrame['roll' + $scope.simpleCounter] = '/';
      } else {
        $scope.rollsFrame['roll' + $scope.simpleCounter] = random_value;
      }
    }
    $scope.game.counterFrames++;
    $scope.simpleCounter++;
    possibleValue2(random_value, values);
    console.log($scope.rollsFrame);
  }

});
