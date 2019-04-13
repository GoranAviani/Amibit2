function confirmaDeletion() {
    var res = confirm("You are about to delete a link. Are you sure?");
      if (res) {
          return true;
      } else {
          return false;
      }
  }