$(function(){
    $(".cell_photo").click(function(){
        $("#modal_thumbnail").data("photo-uid", $(this).data("photo-uid"));
        var file_path = $(this).data("file-path");
        var img_url = '"/static/photos/' + file_path + '"'

        $('#modal_body_photo').css('background-image', 'url(' + img_url + ')');

        create_main_relation_table("#modal_body_photo_main_relation");
        create_sub_relation_table("#modal_body_photo_sub_relation", file_path);

        $("#modal_thumbnail").modal("show");

        return false;
    });

    $('#modal_thumbnail').on('shown.bs.modal', function (event) {
        let photo_uid = $(this).data("photo-uid");

        /*
        $.ajax({
            url: "relation/" + photo_uid,
        }).done(function(data){
            for (let i=0; i < 6; i++) {
                let item = data[i]
                let file_path = item["file_path"];
                let img_url = '"/static/photos/' + file_path + '"';
                $("#main_relation_" + i).css('background-image', 'url(' + img_url + ')');
            }

        }).fail(function(data){
            alert('error!!! : ' + data);
        });
        */

        $.ajax({
            url: "relation/" + photo_uid + "/0/" ,
        }).done(function(data){
            for (let i=0; i < data.length; i++) {
                let item = data[i]
                let file_path = item["file_path"];
                let img_url = '"/static/photos/' + file_path + '"';
                $("#sub_relation_0_" + i).css('background-image', 'url(' + img_url + ')');
            }
        }).fail(function(data){
            alert('error!!! : ' + data);
        });

        $.ajax({
            url: "relation/" + photo_uid + "/5/" ,
        }).done(function(data){
            for (let i=0; i < data.length; i++) {
                let item = data[i]
                let file_path = item["file_path"];
                let img_url = '"/static/photos/' + file_path + '"';
                $("#sub_relation_1_" + i).css('background-image', 'url(' + img_url + ')');
            }
        }).fail(function(data){
            alert('error!!! : ' + data);
        });

        $.ajax({
            url: "relation/" + photo_uid + "/3/" ,
        }).done(function(data){
            for (let i=0; i < data.length; i++) {
                let item = data[i]
                let file_path = item["file_path"];
                let img_url = '"/static/photos/' + file_path + '"';
                $("#sub_relation_2_" + i).css('background-image', 'url(' + img_url + ')');
            }
        }).fail(function(data){
            alert('error!!! : ' + data);
        });

	});
});

//
// Main relation
//
function create_main_relation_table(parent_id) {
    $(parent_id).empty();
    for (var i = 0; i < 6; i++) {
        var element_id = "main_relation_" + i;
        var item = "<div class='col-sm-4 modal_thumbnail_main_row'><div id='" + element_id + "' class='thumbnail'></div></div>";
        $(parent_id).append(item);
    }
}

//
// Sub relation
//
function create_sub_relation_table(parent_id, file_path) {
    $(parent_id).empty();
    $(parent_id).append("<hr />");
    $(parent_id).append("<h5 class='text-center'>全体</h5>");
    $(parent_id).append(get_sub_relation_table_body("1004.jpg", 0));
    $(parent_id).append("<h5 class='text-center'>車両</h5>");
    $(parent_id).append(get_sub_relation_table_body("1000.jpg", 1));
    $(parent_id).append("<h5 class='text-center'>風景</h5>");
    $(parent_id).append(get_sub_relation_table_body("1001.jpg", 2));
    $(parent_id).append("<h5 class='text-center'>カメラアングル</h5>");
    $(parent_id).append(get_sub_relation_table_body("1002.jpg", 3));
    $(parent_id).append("<h5 class='text-center'>地域</h5>");
    $(parent_id).append(get_sub_relation_table_body("1003.jpg", 4));
}

function get_sub_relation_table_body(file_path, index) {
    var table_header =
        "<div class='table-responsive'>" +
            "<table class='table table-striped modal_thumbnail_sub_table'>" +
                "<tbody>" +
                    "<tr>";
    var table_footer =
                    "</tr>" +
                "</tbody>" +
            "</table>" +
        "</div>";
    var table_data = get_sub_relation_table_data(file_path, index)
    return table_header + table_data + table_footer;
}

function get_sub_relation_table_data(file_path, index) {
    var table_data = ""
    for (var i = 0; i < 10; i++) {
        var element_id = "sub_relation_" + index + "_" + i;

        var img_url = '"/static/photos/' + file_path + '"'
        table_data +=
            "<td class='modal_thumbnail_sub_row'>" +
                //"<div class='thumbnail' style='background-image: url(" + img_url + ")'></div>" +
                "<div id='" + element_id + "' class='thumbnail'></div>" +
            "</td>";
    }

    return table_data;
}
