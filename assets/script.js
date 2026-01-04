// Interactive TOC - smooth scrolling and highlight current section
document.addEventListener('DOMContentLoaded', function() {
    const tocLinks = document.querySelectorAll('.toc a');
    const headings = document.querySelectorAll('[id]');

    // Smooth scroll on TOC link click
    tocLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const target = document.getElementById(targetId);
            
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
                // Highlight the clicked link
                tocLinks.forEach(l => l.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });

    // Highlight TOC link based on scroll position
    function updateActiveTocLink() {
        let activeHeading = null;
        
        headings.forEach(heading => {
            const rect = heading.getBoundingClientRect();
            if (rect.top <= 100) {
                activeHeading = heading;
            }
        });

        tocLinks.forEach(link => {
            link.classList.remove('active');
            if (activeHeading) {
                const targetId = link.getAttribute('href').substring(1);
                if (targetId === activeHeading.id) {
                    link.classList.add('active');
                }
            }
        });
    }

    // Update on scroll
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(updateActiveTocLink, 100);
    });

    // Initial update
    updateActiveTocLink();
});

// Copy code block functionality
document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('pre');
    
    codeBlocks.forEach(block => {
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copy';
        button.style.cssText = `
            position: absolute;
            top: 5px;
            right: 5px;
            padding: 5px 10px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 12px;
            z-index: 10;
        `;
        
        block.style.position = 'relative';
        block.appendChild(button);
        
        button.addEventListener('click', function() {
            const code = block.textContent;
            navigator.clipboard.writeText(code).then(() => {
                button.textContent = 'Copied!';
                setTimeout(() => {
                    button.textContent = 'Copy';
                }, 2000);
            });
        });
    });
});

// Active nav item highlighting
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.year-section .nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});
