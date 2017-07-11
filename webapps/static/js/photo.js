$(function(){
    $(".cell_photo").click(function(){
        let photo_uid = $(this).data("photo-uid");
        let file_path = $(this).data("file-path");
        create_modal_body(photo_uid, file_path);
        $("#modal_thumbnail").modal("show");
        return false;
    });

    $('#modal_thumbnail').on('shown.bs.modal', function (event) {
        initialize_relation_image();
	});
});

//
// Modal
//
function create_modal_body(photo_uid, file_path) {
    $("#modal_thumbnail").data("photo-uid", photo_uid);
    let img_url = '"/static/photos/' + file_path + '"'

    $('#modal_body_photo').css('background-image', 'url(' + img_url + ')');

    create_main_relation_table("#modal_body_photo_main_relation");
    create_sub_relation_table(0);
    create_sub_relation_table(1);
    create_sub_relation_table(2);
    create_sub_relation_table(3);
    create_sub_relation_table(4);

    $(".cell_sub_relation_photo").click(function(){
        let photo_uid = $(this).data("photo-uid");
        let file_path = $(this).data("file-path");
        create_modal_body(photo_uid, file_path);
        initialize_relation_image();
        return false;
    });

}

function initialize_relation_image() {
    let photo_uid = $("#modal_thumbnail").data("photo-uid");

    $.ajax({
        url: "relation/" + photo_uid + "/0/",
    }).done(function(data){
        relation = data.relation;
        similarity = data.similarity;
        for (let i=0; i < 6; i++) {
            let item = relation[i];
            console.log(similarity[i]);
            let file_path = item["file_path"];
            let img_url = '"/static/photos/' + file_path + '"';
            $("#main_relation_" + i).css('background-image', 'url(' + img_url + ')');
        }
    }).fail(function(data){
        alert('error!!! : ' + data);
    });

    let relation_param = [
        {relation_type: 0, index: 0},
        {relation_type: 5, index: 1},
        {relation_type: 3, index: 2},
        {relation_type: 1, index: 3},
        {relation_type: 4, index: 4},
    ];

    var photo_info = "ID=" + photo_uid;
    for (let index in relation_param) {
        let param = relation_param[index];
        $.ajax({
            url: "relation/" + photo_uid + "/" + param.relation_type + "/" ,
        }).done(function(data){
            relation = data.relation;
            if (param.index > 0) {
                $("#info_tab" + param.index).text(data.info);
                if (photo_info.length > 0) {
                    photo_info += ",";
                }
                photo_info += data.info;
                $("#modal_title").text(photo_info);
            }
            for (let i=0; i < relation.length; i++) {
                let item = relation[i]
                let file_path = item["file_path"];
                let img_url = '"/static/photos/' + file_path + '"';
                let element_id = "#sub_relation_" + param.index + "_" + i;
                $(element_id).css('background-image', 'url(' + img_url + ')');
                $(element_id).data("photo-uid", item["uid"]);
                $(element_id).data("file-path", item["file_path"]);
            }
        }).fail(function(data){
            alert('error!!! : ' + data);
        });
    }
}

//
// Main relation
//
function create_main_relation_table(parent_id) {
    $(parent_id).empty();
    for (var i = 0; i < 6; i++) {
        var element_id = "main_relation_" + i;
        var item =
            "<div class='col-sm-4 modal_thumbnail_main_row'>" +
                "<a id='" + element_id + "' href='#' class='cell_main_relation_photo thumbnail photo_wrapper'>" +
                    "<div class='photo_info relation'>50%</div>" +
                "</a>" +
            "</div>";
        $(parent_id).append(item);
    }
}

//
// Sub relation
//
function create_sub_relation_table(index) {
    let parent_id = "#tab" + index;
    $(parent_id).empty();
    let table_data = get_sub_relation_table_data(index)
    let table_body =
        "<div class='table-responsive'>" +
            "<table class='table table-striped modal_thumbnail_sub_table'>" +
                "<tbody>" +
                    "<tr>" +
                        table_data +
                    "</tr>" +
                "</tbody>" +
            "</table>" +
        "</div>";
    $(parent_id).append(table_body);
}

function get_sub_relation_table_data(index) {
    var table_data = ""
    for (var i = 0; i < 10; i++) {
        var element_id = "sub_relation_" + index + "_" + i;
        table_data +=
            "<td class='modal_thumbnail_sub_row'>" +
                "<a id='" + element_id + "' href='#' class='cell_sub_relation_photo thumbnail photo_wrapper'>" +
                    "<div class='photo_info relation'>50%</div>" +
                "</a>" +
            "</td>";
    }
    return table_data;
}
