/* ============================================
   GenoWeekly — Main JavaScript
   ============================================ */

(function () {
  "use strict";

  var domainNames = {
    genomics: "基因组学",
    transcriptomics: "转录组学",
    "single-cell": "单细胞组学",
    proteomics: "蛋白质组学",
    epigenomics: "表观遗传学",
    metagenomics: "宏基因组学",
    "spatial-omics": "时空组学",
  };

  // --- Sidebar → scroll to h3 heading ---
  function initSidebarScrolling() {
    var sidebar = document.getElementById("domainSidebar");
    if (!sidebar) return;

    var content = document.querySelector(".post-content");
    if (!content) return;

    sidebar.addEventListener("click", function (e) {
      var btn = e.target.closest(".domain-item");
      if (!btn) return;

      var domain = btn.getAttribute("data-domain");
      var name = domainNames[domain];
      if (!name) return;

      // Update active state
      sidebar.querySelectorAll(".domain-item").forEach(function (el) {
        el.classList.remove("active");
      });
      btn.classList.add("active");

      // Find the first h3 in post-content that contains the domain name
      var headings = content.querySelectorAll("h3");
      for (var i = 0; i < headings.length; i++) {
        if (headings[i].textContent.indexOf(name) !== -1) {
          headings[i].scrollIntoView({ behavior: "smooth", block: "start" });
          break;
        }
      }
    });
  }

  // --- Intro cards → scroll to domain ---
  function initIntroCards() {
    document.querySelectorAll(".domain-intro-card").forEach(function (card) {
      card.addEventListener("click", function () {
        var domain = this.getAttribute("data-domain");
        if (!domain) return;

        // Click the corresponding sidebar button
        var sidebarBtn = document.querySelector(
          '.domain-item[data-domain="' + domain + '"]'
        );
        if (sidebarBtn) {
          sidebarBtn.click();
        }
      });
    });
  }

  // --- Initialize ---
  function init() {
    initSidebarScrolling();
    initIntroCards();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
