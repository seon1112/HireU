$(function() {
  loadInterviewPreparation();

  $(".menu").click(function(){
    $(".menu").removeClass("selected");
    $(this).addClass("selected");
  });
});

function loadInterviewPreparation(){
  $.ajax({
    url: '/load_interview_preparation',  
    type: 'GET',
    success: function(data) {
        $('#interview_content').html(data);
    }
  });
};

function loadUserSettings(){
  $.ajax({
    url: '/load_user_settings',  
    type: 'GET',
    success: function(data) {
        $('#interview_content').html(data);
    }
  });
};
function loadInterviewProcess(){
  $.ajax({
    url: '/load_interview_process',  
    type: 'GET',
    success: function(data) {
        $('#interview_content').html(data);
    }
  });
};

function loadReportGeneration(){
  $.ajax({
    url: '/load_report_generation',  
    type: 'GET',
    success: function(data) {
        $('#interview_content').html(data);
    }
  });
};

function loadInterviewCompletion(){
  $.ajax({
    url: '/load_interview_completion',  
    type: 'GET',
    success: function(data) {
        $('#interview_content').html(data);
    }
  });
};
