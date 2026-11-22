"""Content service — all static content data for the Aurocous website."""


def get_services() -> list[dict]:
    """Return the list of 9 services offered by Aurocous."""
    return [
        {
            "id": "web-development",
            "title": "Web Development",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
            "description": "We design and develop modern web applications that combine intuitive user experiences with reliable backend engineering. Our focus is on performance, maintainability, and solutions aligned with your business objectives.",
            "features": ["Custom Web Applications", "Frontend & Backend Development", "API Development & Integration", "Performance Optimization"],
        },
        {
            "id": "mobile-app-development",
            "title": "Mobile App Development",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
            "description": "We build mobile experiences that help businesses connect with their customers and teams. From concept to implementation, we focus on usability, functionality, and consistent performance across devices.",
            "features": ["iOS & Android Applications", "Cross-Platform Development", "Mobile App Integration", "App Maintenance & Enhancement"],
        },
        {
            "id": "custom-software-development",
            "title": "Custom Software Development",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
            "description": "Every business has unique processes and requirements. We develop tailored software solutions that simplify operations, connect systems, and support the way your organization works.",
            "features": ["Business Software Solutions", "Enterprise Application Development", "System Integration", "Legacy Application Modernization"],
        },
        {
            "id": "ai-machine-learning",
            "title": "AI & Machine Learning",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a4 4 0 0 1 4 4c0 1.95-1.4 3.57-3.25 3.92L12 10v2"/><circle cx="12" cy="16" r="2"/><path d="M12 18v2"/><path d="M8 22h8"/><path d="M7 6a5 5 0 0 0 0 6"/><path d="M17 6a5 5 0 0 1 0 6"/></svg>',
            "description": "We help businesses explore practical applications of artificial intelligence and machine learning to improve workflows, work with data, and create smarter digital experiences.",
            "features": ["AI-Powered Applications", "Machine Learning Solutions", "Intelligent Workflow Automation", "Data-Driven Insights"],
        },
        {
            "id": "cloud-devops",
            "title": "Cloud & DevOps",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>',
            "description": "We help engineering teams improve application delivery and infrastructure management through cloud-oriented development practices, automation, and reliable deployment workflows.",
            "features": ["Cloud Application Development", "CI/CD Automation", "Containerization", "Infrastructure & Deployment Automation"],
        },
        {
            "id": "ui-ux-design",
            "title": "UI/UX Design",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r="2.5"/><circle cx="19" cy="17" r="2"/><circle cx="6" cy="18" r="3"/><path d="M9.59 16.51A5 5 0 0 1 13.5 9a5 5 0 0 1 4.77 3.5"/></svg>',
            "description": "We create digital experiences that make complex interactions feel simple. Our design process combines user understanding, clear visual communication, and usability-focused interfaces.",
            "features": ["User Experience Design", "Interface Design", "Wireframes & Prototypes", "Design Systems"],
        },
        {
            "id": "ecommerce",
            "title": "E-commerce Development",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>',
            "description": "We develop e-commerce experiences that make online shopping easier for customers and store management more efficient for businesses.",
            "features": ["Custom E-commerce Platforms", "Shopping Cart & Checkout", "Payment Gateway Integration", "Store & Order Management"],
        },
        {
            "id": "crm-erp",
            "title": "CRM & ERP Solutions",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18"/><path d="M3 12h18"/><path d="M8 7h1"/><path d="M15 7h1"/><path d="M8 17h1"/><path d="M15 17h1"/></svg>',
            "description": "We develop and integrate business management solutions that help organizations manage customer relationships, streamline operations, and improve access to business information.",
            "features": ["Custom CRM Development", "ERP Solutions", "Business Process Automation", "Third-Party System Integration"],
        },
        {
            "id": "data-engineering",
            "title": "Data Engineering",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4.03 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/></svg>',
            "description": "We help businesses organize and process data through structured data pipelines and integration solutions, making information more accessible for reporting and informed decision-making.",
            "features": ["Data Pipeline Development", "Data Integration", "ETL Workflows", "Reporting & Analytics Solutions"],
        },
    ]


def get_industries() -> list[dict]:
    """Return the list of 6 industries served by Aurocous."""
    return [
        {
            "id": "healthcare",
            "title": "Healthcare",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
            "description": "Digital solutions that support healthcare workflows, patient engagement, appointment management, and information access.",
        },
        {
            "id": "finance",
            "title": "Finance & Banking",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
            "description": "Software solutions for financial workflows, payment integrations, reporting, and operational processes.",
        },
        {
            "id": "ecommerce-retail",
            "title": "E-commerce & Retail",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
            "description": "Digital commerce experiences, store management systems, inventory workflows, and customer-facing applications.",
        },
        {
            "id": "education",
            "title": "Education & EdTech",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1.1 2.69 2 6 2s6-.9 6-2v-5"/></svg>',
            "description": "Learning platforms, education management systems, digital classrooms, and tools that support learning experiences.",
        },
        {
            "id": "real-estate",
            "title": "Real Estate",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
            "description": "Property management platforms, listing portals, and virtual tour solutions.",
        },
        {
            "id": "logistics",
            "title": "Logistics & Supply Chain",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            "description": "Software solutions for operational visibility, workflow management, inventory coordination, and logistics processes.",
        },
    ]


def get_approach_steps() -> list[dict]:
    """Return the list of 5 approach steps."""
    return [
        {
            "number": "01",
            "title": "Discovery",
            "description": "We understand your business objectives, challenges, users, and project requirements. This gives us the context needed to define the right solution.",
        },
        {
            "number": "02",
            "title": "Strategy",
            "description": "We translate requirements into a practical technical direction, identifying the solution architecture, technology choices, scope, and key milestones.",
        },
        {
            "number": "03",
            "title": "Design",
            "description": "We shape the user experience and interface around usability, clarity, and your business identity before moving into development.",
        },
        {
            "number": "04",
            "title": "Development",
            "description": "We build, integrate, and test the solution with a focus on code quality, maintainability, performance, and reliable functionality.",
        },
        {
            "number": "05",
            "title": "Launch & Evolve",
            "description": "We support deployment and help refine the solution as requirements change, keeping future improvements and business growth in mind.",
        },
    ]


def get_reasons() -> list[dict]:
    """Return the list of 6 reasons to choose Aurocous."""
    return [
        {
            "title": "Engineering with Purpose",
            "description": "We focus on solving the actual problem behind every requirement, choosing practical technical approaches instead of adding unnecessary complexity.",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1.08-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09a1.65 1.65 0 0 0 1.51-1.08 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9c.26.604.852.997 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
        },
        {
            "title": "Business-First Thinking",
            "description": "We consider your business goals, users, and operational needs throughout the development process.",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
        },
        {
            "title": "Thoughtful Architecture",
            "description": "We prioritize clean code, maintainable systems, and technical foundations that support future improvements.",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>',
        },
        {
            "title": "End-to-End Collaboration",
            "description": "From initial discussions to implementation, we work closely with you to maintain clarity and alignment throughout the project.",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
        },
        {
            "title": "Transparent Communication",
            "description": "We value clear expectations, regular updates, and open communication at every stage of development.",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
        },
        {
            "title": "Long-Term Perspective",
            "description": "We build with maintainability and adaptability in mind, helping solutions remain useful as business requirements evolve.",
            "icon_svg": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>',
        },
    ]


def get_products() -> list[dict]:
    """Return the list of products (kept for future modularity)."""
    return []


def get_stats() -> list[dict]:
    """Return stats (empty as per specification)."""
    return []


def get_countries() -> list[str]:
    """Return a list of ~50 countries with India first, then alphabetical."""
    return [
        "India",
        "Afghanistan",
        "Argentina",
        "Australia",
        "Austria",
        "Bangladesh",
        "Belgium",
        "Brazil",
        "Canada",
        "Chile",
        "China",
        "Colombia",
        "Czech Republic",
        "Denmark",
        "Egypt",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hong Kong",
        "Hungary",
        "Indonesia",
        "Ireland",
        "Israel",
        "Italy",
        "Japan",
        "Kenya",
        "Malaysia",
        "Mexico",
        "Netherlands",
        "New Zealand",
        "Nigeria",
        "Norway",
        "Pakistan",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Qatar",
        "Romania",
        "Saudi Arabia",
        "Singapore",
        "South Africa",
        "South Korea",
        "Spain",
        "Sri Lanka",
        "Sweden",
        "Switzerland",
        "Thailand",
        "Turkey",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "Vietnam",
    ]
