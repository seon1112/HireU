$(function() {
  $(".history_item_wrap").click(function(){
    var question_list=$(this).closest(".history_item_box").find(".question_list");
    if(question_list.hasClass("show")){
      question_list.removeClass("show");
    }else{
      question_list.addClass("show");
    }
  });

  $("#start_question_btn").click(function(){
    /*
    체크박스 선택 여부 확인하는 코드 추가 필요
    1개 이하면 체크박스를 1가지 이상 선택해주세요
    */
    $("#questionCheckModal").show();
    openModal();
  });

  $("#close_check_question_btn").click(function(){
    $("#questionCheckModal").hide();
    closeModal();
  });

  $("#historyModal").click(function(event) {
    if ($(event.target).is(".modal")) {  
      $(this).hide();
      closeHistoryModal();
      closeModal();
    }
  });
});

/*history모달 닫을 시 기존 선택 정보 모두 삭제 */
function closeHistoryModal(){
  $(".question_list").removeClass('show');
  $(".question_list > .question_item > input[type='checkbox']").prop('checked',false);
}
