$(function(){
    $(".cell_photo").click(function(){
        $("#modal_thumbnail").data("photo-uid", $(this).data("photo-uid"));
        var file_path = $(this).data("file-path");
        var img_url = '"/static/photos/' + file_path + '"'

        $('#modal_body_photo').css('background-image', 'url(' + img_url + ')');

        create_main_relation_table("#modal_body_photo_main_relation");
        create_sub_relation_table(0);
        create_sub_relation_table(1);
        create_sub_relation_table(2);
        create_sub_relation_table(3);
        create_sub_relation_table(4);

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

        let relation_param = [
            {relation_type: 0, index: 0},
            {relation_type: 5, index: 1},
            {relation_type: 3, index: 2},
            {relation_type: 1, index: 3},
            {relation_type: 4, index: 4},
        ];

        for (let index in relation_param) {
            let param = relation_param[index];
            $.ajax({
                url: "relation/" + photo_uid + "/" + param.relation_type + "/" ,
            }).done(function(data){
                relation = data.relation;
                if (param.index > 0) {
                    $("#info_tab" + param.index).text(data.info);
                }
                for (let i=0; i < relation.length; i++) {
                    let item = relation[i]
                    let file_path = item["file_path"];
                    let img_url = '"/static/photos/' + file_path + '"';
                    $("#sub_relation_" + param.index + "_" + i).css('background-image', 'url(' + img_url + ')');
                }
            }).fail(function(data){
                alert('error!!! : ' + data);
            });
        }
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
function create_sub_relation_table(index) {
    let parent_id = "#tab" + index;
    $(parent_id).empty();
    let table_header =
        "<div class='table-responsive'>" +
            "<table class='table table-striped modal_thumbnail_sub_table'>" +
                "<tbody>" +
                    "<tr>";
    let table_footer =
                    "</tr>" +
                "</tbody>" +
            "</table>" +
        "</div>";
    let table_data = get_sub_relation_table_data(index)
    $(parent_id).append(table_header + table_data + table_footer);
}

function get_sub_relation_table_data(index) {
    var table_data = ""
    for (var i = 0; i < 10; i++) {
        var element_id = "sub_relation_" + index + "_" + i;
        table_data +=
            "<td class='modal_thumbnail_sub_row'>" +
                "<div id='" + element_id + "' class='thumbnail'></div>" +
            "</td>";
    }
    return table_data;
}
