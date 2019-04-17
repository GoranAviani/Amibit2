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