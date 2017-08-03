const history_size = 5;
const relation_param = [
    {relation_type: 0, index: 0},
    {relation_type: 5, index: 1},
    {relation_type: 3, index: 2},
    {relation_type: 1, index: 3},
    {relation_type: 4, index: 4},
];

var view_history = [];
var current_type_similarity = {};

$(function(){
    $(".cell_photo").click(function(){
        let photo_uid = $(this).data("photo-uid");
        let file_path = $(this).data("file-path");
        update_view_history(photo_uid);
        create_modal_body(0, photo_uid, file_path);
        $("#modal_thumbnail").modal("show");
        return false;
    });

    $('#modal_thumbnail').on('shown.bs.modal', function (event) {
        initialize_relation_image();
	});
});

function update_view_history(photo_uid) {
    view_history.unshift(photo_uid);
    if (view_history.length > history_size) {
        view_history.pop();
    }
    console.log(view_history);
}

//
// Modal
//
function create_modal_body(pre_photo_uid, photo_uid, file_path) {
    $("#modal_thumbnail").data("pre-photo-uid", pre_photo_uid);
    $("#modal_thumbnail").data("photo-uid", photo_uid);
    let img_url = '"/static/photos/' + file_path + '"'

    $('#modal_body_photo').css('background-image', 'url(' + img_url + ')');

    create_main_relation_table("#modal_body_photo_main_relation");
    create_sub_relation_table(0);
    create_sub_relation_table(1);
    create_sub_relation_table(2);
    create_sub_relation_table(3);
    create_sub_relation_table(4);

    $(".cell_relation_photo").click(function(){
        relation_photo_clicked(this);
        return false;
    });
}

function relation_photo_clicked(element) {
    let pre_photo_uid = $("#modal_thumbnail").data("photo-uid");
    let photo_uid = $(element).data("photo-uid");
    let file_path = $(element).data("file-path");
    update_view_history(photo_uid);
    create_modal_body(pre_photo_uid, photo_uid, file_path);
    initialize_relation_image();
}

function initialize_relation_image() {
    let pre_photo_uid = $("#modal_thumbnail").data("pre-photo-uid");
    let photo_uid = $("#modal_thumbnail").data("photo-uid");
    let history_value = view_history.join('x');

    //
    // main relation
    //

    $.ajax({
        url: "relation/" + history_value + "/",
    }).done(function(data){
        let relation = data.relation;
        let similarity = data.similarity;
        let type_similarity = data.type_similarity;
        for (let i=0; i < 6; i++) {
            initialize_relation_cell(
                relation[i], similarity[i],
                "#main_relation_" + i,
                "#main_relation_info_" + i);
        }
        if (type_similarity) {
            for (key in type_similarity) {
                if (key in current_type_similarity) {
                    current_type_similarity[key] = (current_type_similarity[key] + type_similarity[key]) / 2;
                } else {
                    current_type_similarity[key] = type_similarity[key];
                }
            }
        }
    }).fail(function(data){
        console.log('error!!! : ' + data);
    });

    //
    // sub relation
    //

    var photo_info = "ID=" + photo_uid;
    for (let index in relation_param) {
        let param = relation_param[index];
        $.ajax({
            url: "relation/" + pre_photo_uid + "/" + photo_uid + "/" + param.relation_type + "/" ,
        }).done(function(data){
            let relation = data.relation;
            let similarity = data.similarity;
            if (param.index > 0) {
                let s = Math.round(current_type_similarity[param.relation_type] * 100);
                $("#info_tab" + param.index).text(data.info + " : " + s + "%");
                if (photo_info.length > 0) {
                    photo_info += ",";
                }
                photo_info += data.info;
                $("#modal_title").text(photo_info);
            }
            for (let i=0; i < relation.length; i++) {
                initialize_relation_cell(
                    relation[i], similarity[i],
                    "#sub_relation_" + param.index + "_" + i,
                    "#sub_relation_info_" + param.index + "_" + i);
            }
        }).fail(function(data){
            console.log('error!!! : ' + data);
        });
    }
}

function initialize_relation_cell(item, similarity, element_cell_id, element_info_id) {
    let file_path = item["file_path"];
    let img_url = '"/static/photos/' + file_path + '"';
    $(element_cell_id).css('background-image', 'url(' + img_url + ')');
    $(element_cell_id).data("photo-uid", item["uid"]);
    $(element_cell_id).data("file-path", item["file_path"]);
    let s = Math.round(similarity * 100);
    $(element_info_id).text(s + "%");
}

//
// Main relation
//
function create_main_relation_table(parent_id) {
    $(parent_id).empty();
    for (let i = 0; i < 6; i++) {
        let element_cell_id = "main_relation_" + i;
        let element_info_id = "main_relation_info_" + i;
        let item =
            "<div class='col-sm-4 modal_thumbnail_main_row'>" +
                "<a id='" + element_cell_id + "' href='#' class='cell_relation_photo thumbnail photo_wrapper'>" +
                    "<div id='" + element_info_id + "' class='photo_info relation'></div>" +
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
    for (let i = 0; i < 10; i++) {
        let element_cell_id = "sub_relation_" + index + "_" + i;
        let element_info_id = "sub_relation_info_" + index + "_" + i;
        table_data +=
            "<td class='modal_thumbnail_sub_row'>" +
                "<a id='" + element_cell_id + "' href='#' class='cell_relation_photo thumbnail photo_wrapper'>" +
                    "<div id='" + element_info_id + "' class='photo_info relation'></div>" +
                "</a>" +
            "</td>";
    }
    return table_data;
}
