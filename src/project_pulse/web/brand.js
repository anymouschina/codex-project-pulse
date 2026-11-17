/* Base artwork never includes a notification; the read state owns the badge. */
"use strict";
(() => {
  const favicon = document.querySelector("#app-icon");
  const baseIcon = favicon.href;
  const unreadIcon = favicon.dataset.unreadIcon;
  let previous = null;
  window.PulseBrand = {
    update(snapshot, unavailable = false) {
      const badge = snapshot?.unreadBadge;
      const count = !unavailable && badge?.known === true ? badge.count : 0;
      const unread = count > 0;
      document.title = `${unread ? `(${count}) ` : ""}Project Pulse · 项目总控台`;
      if (previous !== unread) favicon.href = unread ? unreadIcon : baseIcon;
      previous = unread;
    },
  };
})();
