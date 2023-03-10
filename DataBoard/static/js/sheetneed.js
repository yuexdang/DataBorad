var SaveSwitch = document.getElementById("SaveSwitch").innerText;


S_save = document.getElementById("switch-1");
FileUrl = document.getElementById("RenameURL");
FileName = document.getElementById("RenameFile");

Page_init(SaveSwitch);

S_save.addEventListener("click", DataSaveChange);
FileUrl.addEventListener("click", FileUrlChange);
FileName.addEventListener("click", FileNameChange)


function Page_init(SwitchA) {
    if(SwitchA == 'True') {
        S_save.setAttribute("checked", "");
    }
}

function DataSaveChange() {
    if(SaveSwitch == 'True') {
        PostData("isSave","False");
        SaveSwitch = 'False';
    } else {
        PostData("isSave","True");
        SaveSwitch = 'True';
       }
}

function PostData(ChangeKey, ChangeValue) {
    var PD = {
        [ChangeKey] : ChangeValue,
    };
    $.ajax({
        type: "POST",
        url: "/conf",
        data: JSON.stringify(PD),
        contentType: 'application/json',
        success: function (data) { },
    });
}

function FileUrlChange() {
    var FUrl = document.getElementById("file-1");
    var FUrlResult = FUrl.value.replaceAll(" ","^")
    if(FUrl.value.length) {
        PostData("FileURL", FUrlResult);
        FUrl.placeholder = FUrl.value;
    }
    location.reload();
}

function FileNameChange() {
    var FName = document.getElementById("file-2");
    var FNameResult = FName.value.replaceAll(" ","^")
    if(FName.value.length) {
        PostData("Filename", FNameResult);
        FName.placeholder = FName.value;
    }
    location.reload();
}