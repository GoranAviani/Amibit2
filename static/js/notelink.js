var screen_width = window.innerWidth;
var screen_height = window.innerHeight;

window.onload = function() {
    if(screen_width <= 768) {
      document.getElementById("DashboardNotes").style.display = "none";
      document.getElementById("DashboardLinks").style.display = "none";
    }
  };
  


  function toggle_notes() {
    var x = document.getElementById("DashboardNotes");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggle_links() {
    var x = document.getElementById("DashboardLinks");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}




function confirmLinkDeletion() {
    var res = confirm("You are about to delete a link. Are you sure?");
      if (res) {
          return true;
      } else {
          return false;
      }
  }


function confirmNoteDeletion() {
var res = confirm("You are about to delete a note. Are you sure?");
    if (res) {
        return true;
    } else {
        return false;
    }
}

