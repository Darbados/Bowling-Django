let values = [0,1,2,3,4,5,6,7,8,9,10];
let current_frame = Number($('.frame').val())+1;
let rolls = [];
let current_roll = Number($(".counter_rolls").val());
let random_value = 0
let total = 0;

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

//handle the rolls, including check for strike and spare
$("input[type=button]").on('click', function(){

  if (current_frame < 10){
    $('#id_attempt3').val(0);
    if (current_roll == 1){
      //for testing purposes
      console.log(`Frame: ${current_frame}, Roll: ${current_roll}`);

       random_value = values[Math.floor((Math.random()*values.length))];
      //fill the attempt 1 field with the result from the first roll
      $("#id_attempt1").val(random_value);
      $('.table').find('td').eq(current_roll-1).find('.place').val(random_value);

      rolls.push({roll: current_roll, result: random_value})

      //udpating the roll counter for the second attempt.
      current_roll++;
      $(".counter_rolls").val(current_roll)

      if (random_value == 10){
        $("#id_attempt2").val(0);
        $('.table').find('td').eq(current_roll-1).find('.place').val('-');

        rolls.push({roll: current_roll, result: 0});
        total = 10;

        $(this).addClass('hidden');
        $("input[type=submit]").removeClass('hidden');
      } else {
        $(this).addClass('hidden');
        $("#roll"+current_roll).removeClass('hidden');
      }
    } else if (current_roll == 2 && rolls.length < 2){
      console.log(`Frame: ${current_frame}, Roll: ${current_roll}`);
      possibleValue2(random_value);

      random_value = values[Math.floor((Math.random()*values.length))];

      //fill the attempt 1 field with the result from the first roll
      $("#id_attempt2").val(random_value);

      //fill the appropriate box in the scoreboard
      $('.table').find('td').eq(current_roll-1).find('.place').val((random_value + rolls[0].result) < 10 ? random_value : '/')

      rolls.push({roll: current_roll, result: random_value})
      $(this).addClass('hidden');
      $("input[type=submit]").removeClass('hidden');
    }
  } else {
    if (current_roll == 1){
      //for testing purposes
      console.log(`Frame: ${current_frame}, Roll: ${current_roll}`);

      random_value = values[Math.floor((Math.random()*values.length))];

      //fill the attempt 1 field with the result from the first roll
      $("#id_attempt" + current_roll).val(random_value);

      //fill the appropriate box in the scoreboard
      $('.table').find('td').eq(current_roll-1).find('.place').val(random_value == 10 ? 'X' : random_value)

      rolls.push({roll: current_roll, result: random_value})

      //udpating the roll counter for the second attempt.
      current_roll++;
      $(".counter_rolls").val(current_roll)

      if (random_value == 10){
        $("#id_attempt2").val(0);
        $('.table').find('td').eq(current_roll-1).find('.place').val('-');
        rolls.push({roll: current_roll, result: 0});
        total = 10;
        $(this).addClass('hidden');
        $("#roll"+(++current_roll)).removeClass('hidden');
      } else {
        $(this).addClass('hidden');
        $("#roll"+current_roll).removeClass('hidden');
      }
    } else if (current_roll == 2 && rolls.length < 2){
      console.log(`Frame: ${current_frame}, Roll: ${current_roll}`);

      possibleValue2(random_value);
      random_value = values[Math.floor((Math.random()*values.length))];

      //fill the attempt 1 field with the result from the first roll
      $("#id_attempt" + current_roll).val(random_value);

      //fill the appropriate box in the scoreboard
      $('.table').find('td').eq(current_roll-1).find('.place').val((random_value + rolls[0].result) < 10 ? random_value : '/')

      rolls.push({roll: current_roll, result: random_value})
      current_roll++;

      for (let roll of rolls) total += roll.result;

      if (total == 10) {
        $(this).addClass('hidden');
        $("#roll" + current_roll).removeClass('hidden');
      } else {
        $("#id_attempt" + current_roll).val(0);
        $('.table').find('td:last').addClass('hidden');
        $(this).addClass('hidden');
        $("input[type=submit]").removeClass('hidden');
      }
    } else {
      console.log(`Frame: ${current_frame}, Roll: ${current_roll}`);

      $("#id_attempt" + current_roll).val(random_value);
      $('.table').find('td').eq(current_roll-1).find('.place').val(random_value == 10 ? 'X' : random_value);

      $(this).addClass('hidden');
      $("input[type=submit]").removeClass('hidden');
    }
  }
  console.log(rolls,total);
});
