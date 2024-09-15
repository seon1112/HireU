$(function() {
  // 모달 열기 버튼을 클릭하면 해당 모달을 보여줌
  $(".open_modal").click(function() {
    const modalId = $(this).data("modal");  
    $("#" + modalId).show();
    openModal();
  });

  // 모달 닫기 버튼을 클릭하면 해당 모달을 숨김
  $(".modal .close").click(function() {
    $(this).closest(".modal").hide();
    closeModal();
  });

  // 모달 외부 클릭 시 모달 닫기
  $(".modal").click(function(event) {
    if ($(event.target).is(".modal")) {  
      $(this).hide();
      closeModal();
    }
  });

});

// 모달을 열 때
function openModal() {
  $("body").css("overflow", "hidden");  
}

// 모달을 닫을 때
function closeModal() {
  $("body").css("overflow", "");  
}