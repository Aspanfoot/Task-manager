	$(function () {

var loadForm = function () {
	var btn = $(this);
	$.ajax({
		url: btn.attr("data-url"),
		type: 'get',
		dataType: 'json',
		beforeSend: function () {
		$("#modal-task").modal("show");
			},
		success: function (data) {
		$("#modal-task .modal-content").html(data.html_form);
		}
	});
};

var saveForm = function () {
	var form = $(this);
	$.ajax({
		url: form.attr("action"),
		data: form.serialize(),
		type: form.attr("method"),
		dataType: 'json',
		success: function (data) {
			if (data.form_is_valid) {
				$("#task-table tbody").html(data.html_task_list);
				$("#modal-task").modal("hide");
			}
		else {
			$("#modal-task .modal-content").html(data.html_form);
			}
		}
	});
	return false;
};

// Створюємо таск
$(".js-create-task").click(loadForm);
$("#modal-task").on("submit", ".js-task-add-form", saveForm);

// Оновлюємо таск
$("#task-table").on("click", ".js-update-task", loadForm);
$("#modal-task").on("submit", ".js-task-update-form", saveForm);

// Видаляємо таск
$("#task-table").on("click", ".js-delete-task", loadForm);
$("#modal-task").on("submit", ".js-task-delete-form", saveForm);

});