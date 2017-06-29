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
        $.ajax({
            url: "main_relation/" + photo_uid,

        }).done(function(data){
            for (let i=0; i < data.length; i++) {
                let file_path = data[i];
                let img_url = '"/static/photos/' + file_path + '"';
                $("#main_relation_" + i).css('background-image', 'url(' + img_url + ')');
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
    $(parent_id).append("<h5 class='text-center'>Hello. Some text here.</h5>");
    $(parent_id).append(get_sub_relation_table_body("1000.jpg"));
    $(parent_id).append(get_sub_relation_table_body("1001.jpg"));
    $(parent_id).append(get_sub_relation_table_body("1002.jpg"));
    $(parent_id).append(get_sub_relation_table_body("1003.jpg"));
    $(parent_id).append(get_sub_relation_table_body("1004.jpg"));
}

function get_sub_relation_table_body(file_path) {
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
    var table_data = get_sub_relation_table_data(file_path)
    return table_header + table_data + table_footer;
}

function get_sub_relation_table_data(file_path) {
    var table_data = ""
    for (var i = 0; i < 10; i++) {
        var img_url = '"/static/photos/' + file_path + '"'
        table_data +=
            "<td class='modal_thumbnail_sub_row'>" +
                "<div class='thumbnail' style='background-image: url(" + img_url + ")'></div>" +
            "</td>";
    }
    return table_data;
}
