(function () {
  "use strict";

  var domainMap = {
    "基因组学": "genomics",
    "转录组学": "transcriptomics",
    "单细胞组学": "single-cell",
    "蛋白质组学": "proteomics",
    "表观遗传学": "epigenomics",
    "宏基因组学": "metagenomics",
    "时空组学": "spatial-omics",
  };

  var domainInfo = {
    genomics: { cn: "基因组学", en: "Genomics" },
    transcriptomics: { cn: "转录组学", en: "Transcriptomics" },
    "single-cell": { cn: "单细胞组学", en: "Single-cell" },
    proteomics: { cn: "蛋白质组学", en: "Proteomics" },
    epigenomics: { cn: "表观遗传学", en: "Epigenomics" },
    metagenomics: { cn: "宏基因组学", en: "Metagenomics" },
    "spatial-omics": { cn: "时空组学", en: "Spatial-omics" },
  };

  var orderedDomains = [
    "genomics",
    "transcriptomics",
    "single-cell",
    "proteomics",
    "epigenomics",
    "metagenomics",
    "spatial-omics",
  ];

  // --- Reorganize post content into domain panels ---
  function initPanelSystem() {
    var content = document.querySelector(".post-content");
    if (!content || content.dataset.panelsReady) return;

    var children = Array.from(content.children);
    if (children.length === 0) return;

    // Only run if the content has domain h3 headings
    var hasDomain = children.some(function (el) {
      if (el.tagName !== "H3") return false;
      var text = el.textContent;
      return Object.keys(domainMap).some(function (cn) {
        return text.indexOf(cn) !== -1;
      });
    });
    if (!hasDomain) return;

    // Walk children collecting content by domain
    var panels = {};
    var frontierNodes = [];
    var currentSection = null;
    var currentDomain = null;
    var inFrontier = false;

    for (var i = 0; i < children.length; i++) {
      var el = children[i];
      var tag = el.tagName;

      if (tag === "HR") continue;

      if (tag === "H2") {
        var t = el.textContent;
        // Detect frontier section
        if (t.indexOf("前沿进展") !== -1) {
          inFrontier = true;
          frontierNodes.push(el);
          continue;
        }
        inFrontier = false;
        if (t.indexOf("新工具") !== -1 || t.indexOf("数据库") !== -1) {
          currentSection = "tools";
        } else if (t.indexOf("新方法") !== -1 || t.indexOf("论文") !== -1) {
          currentSection = "papers";
        } else {
          currentSection = null;
        }
        currentDomain = null;
        continue;
      }

      if (inFrontier) {
        frontierNodes.push(el);
        continue;
      }

      if (tag === "H3") {
        currentDomain = null;
        var h3t = el.textContent;
        for (var cn in domainMap) {
          if (h3t.indexOf(cn) !== -1) {
            currentDomain = domainMap[cn];
            if (!panels[currentDomain])
              panels[currentDomain] = { tools: [], papers: [] };
            break;
          }
        }
        continue;
      }

      // Regular content — associate with current domain + section
      if (currentDomain && currentSection && panels[currentDomain]) {
        panels[currentDomain][currentSection].push(el);
      }
    }

    // Filter to domains that have content
    var activeDomains = orderedDomains.filter(function (k) {
      return (
        panels[k] &&
        (panels[k].tools.length > 0 || panels[k].papers.length > 0)
      );
    });
    if (activeDomains.length === 0) return;

    content.dataset.panelsReady = "true";

    // Save original content as hidden fallback (noscript / SEO)
    var fallback = document.createElement("div");
    fallback.style.display = "none";
    while (content.firstChild) fallback.appendChild(content.firstChild);
    content.appendChild(fallback);

    // Build domain panels
    activeDomains.forEach(function (key) {
      var info = domainInfo[key];
      var pd = panels[key];
      if (!info) return;

      var panel = document.createElement("div");
      panel.className =
        "domain-panel" + (key === activeDomains[0] ? " active" : "");
      panel.id = "panel-" + key;

      // Panel title
      var title = document.createElement("h3");
      title.className = "domain-panel-title";
      title.innerHTML = info.cn + ' <span class="en-tag">' + info.en + "</span>";
      panel.appendChild(title);

      // Tools subsection
      if (pd.tools.length > 0) {
        var st = document.createElement("div");
        st.className = "section-subheader";
        st.innerHTML = '<span class="icon">🛠</span> 新工具与数据库更新';
        panel.appendChild(st);
        pd.tools.forEach(function (n) {
          panel.appendChild(n.cloneNode(true));
        });
      }

      // Papers subsection
      if (pd.papers.length > 0) {
        var sp = document.createElement("div");
        sp.className = "section-subheader";
        sp.innerHTML = '<span class="icon">📄</span> 新方法与论文';
        panel.appendChild(sp);
        pd.papers.forEach(function (n) {
          panel.appendChild(n.cloneNode(true));
        });
      }

      content.appendChild(panel);
    });

    // Append frontier section
    if (frontierNodes.length > 0) {
      var fw = document.createElement("div");
      fw.className = "frontier-section";
      frontierNodes.forEach(function (n) {
        fw.appendChild(n.cloneNode(true));
      });
      content.appendChild(fw);
    }

  }

  // --- Switch active domain panel ---
  function showDomain(domain) {
    // Sidebar active state
    var sidebar = document.getElementById("domainSidebar");
    if (sidebar) {
      sidebar.querySelectorAll(".domain-item").forEach(function (el) {
        el.classList.remove("active");
      });
      var btn = sidebar.querySelector(
        '.domain-item[data-domain="' + domain + '"]'
      );
      if (btn) btn.classList.add("active");
    }

    // Panel visibility
    document.querySelectorAll(".domain-panel").forEach(function (p) {
      p.classList.remove("active");
    });
    var panel = document.getElementById("panel-" + domain);
    if (panel) {
      panel.classList.add("active");
    }

    // Scroll content area into view
    var dc = document.querySelector(".domain-content");
    if (dc) {
      dc.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  // --- Sidebar click handler ---
  function initSidebar() {
    var sidebar = document.getElementById("domainSidebar");
    if (!sidebar) return;
    sidebar.addEventListener("click", function (e) {
      var btn = e.target.closest(".domain-item");
      if (!btn) return;
      var domain = btn.getAttribute("data-domain");
      if (domain) showDomain(domain);
    });
  }

  // --- Intro card click handler ---
  function initIntroCards() {
    document.querySelectorAll(".domain-intro-card").forEach(function (card) {
      card.addEventListener("click", function () {
        var domain = this.getAttribute("data-domain");
        if (domain) showDomain(domain);
      });
    });
  }

  // --- Initialize on pages with sidebar ---
  function init() {
    if (!document.getElementById("domainSidebar")) return;
    initPanelSystem();
    initSidebar();
    initIntroCards();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
