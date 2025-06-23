import os
import textwrap

# --- CONTEÚDO DOS ARQUIVOS ---
# Cada variável aqui contém o texto completo de um arquivo do projeto.

PACKAGE_JSON_CONTENT = """
{
  "name": "portfolio-gabriel-alves",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "gsap": "^3.12.5",
    "lucide": "^0.395.0",
    "typeit": "^8.8.3"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.4",
    "vite": "^5.3.1"
  }
}
"""

TAILWIND_CONFIG_JS_CONTENT = """
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./404.html",
    "./pages/**/*.{html,js}",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class', // Habilita o dark mode baseado em classe
  theme: {
    extend: {
      colors: {
        'amarelo-principal': '#FFD700',
        'amarelo-secundario': '#f59e0b',
      }
    },
  },
  plugins: [],
}
"""

POSTCSS_CONFIG_JS_CONTENT = """
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

GITIGNORE_CONTENT = """
# Dependencies
/node_modules

# Build output
/dist

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Environment variables
.env
.env*.local

# IDE files
.idea
.vscode
*.swo
"""

INDEX_HTML_CONTENT = """
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gabriel Alves - Desenvolvedor de Software e Soluções Digitais</title>
    
    <meta name="description" content="Especialista em automação e soluções digitais focado em redução de custos, aumento de vendas e eficiência operacional, com domínio em React, Flutter e metodologias ágeis.">
    <meta property="og:title" content="Gabriel Alves - Especialista em Automação e Soluções Digitais">
    <meta property="og:description" content="Transformo desafios de negócio em aplicações robustas e de alta performance. Veja meus projetos e resultados.">
    <meta property="og:image" content="https://i.ibb.co/8DPzTV1n/Imagem-do-Whats-App-de-2025-06-23-s-14-27-25-77448b47.jpg"> 
    <meta property="og:url" content="https://skreew.github.io/gcruz/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">

    <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
    <link rel="manifest" href="/site.webmanifest" />
    <meta name="theme-color" content="#000000">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Gabriel Alves da Cruz",
      "jobTitle": "Especialista em Automação e Soluções Digitais",
      "url": "https://skreew.github.io/gcruz/",
      "image": "https://i.ibb.co/8DPzTV1n/Imagem-do-Whats-App-de-2025-06-23-s-14-27-25-77448b47.jpg",
      "worksFor": { "@type": "Organization", "name": "Freelancer" },
      "alumniOf": { "@type": "CollegeOrUniversity", "name": "Jalasoft" },
      "knowsAbout": ["Automação", "Python", "JavaScript", "Google Apps Script", "RPA", "WordPress", "WooCommerce", "SEO", "Metodologias Ágeis"],
      "sameAs": ["https://www.linkedin.com/in/gabriel-alves-da-cruz-692484223", "https://github.com/skreew"]
    }
    </script>
</head>
<body class="bg-white dark:bg-black text-gray-800 dark:text-gray-100 antialiased">

    <noscript><div class="bg-amarelo-principal text-black p-4 text-center fixed top-0 w-full z-[9999]">Este site funciona melhor com JavaScript habilitado.</div></noscript>
    <a href="#main-content" class="skip-link">Pular para o conteúdo principal</a>
    <canvas id="background-canvas" class="fixed top-0 left-0 w-full h-full -z-10"></canvas>

    <header id="main-header" class="fixed top-0 left-0 w-full p-2 sm:p-4 z-50">
        <div class="container mx-auto flex justify-between items-center glass-effect rounded-full py-2 px-4 sm:py-3 sm:px-6">
            <a href="#" class="text-lg sm:text-xl font-bold text-inherit whitespace-nowrap">Gabriel Alves<span class="text-amarelo-principal">.</span></a>
            <nav id="main-nav" class="hidden md:flex space-x-6 lg:space-x-8 items-center text-sm lg:text-base">
                <a href="#about" class="nav-link">Perfil</a>
                <a href="#skills" class="nav-link">Competências</a>
                <a href="#projects" class="nav-link">Projetos</a>
                <a href="#results" class="nav-link">Resultados</a>
                <a href="#certifications" class="nav-link">Cursos</a>
                <a href="#contact" class="nav-link">Contato</a>
            </nav>
            <div class="flex items-center gap-2 sm:gap-4">
                 <button id="theme-toggle" aria-label="Alternar tema" class="text-inherit hover:text-amarelo-principal transition-colors p-1">
                     <i data-lucide="sun" class="w-5 h-5 sm:w-6 sm:h-6 hidden" id="sun-icon"></i>
                     <i data-lucide="moon" class="w-5 h-5 sm:w-6 sm:h-6 hidden" id="moon-icon"></i>
                 </button>
                 <button id="hamburger-btn" aria-label="Abrir menu" aria-expanded="false" class="md:hidden z-[101] text-inherit p-1">
                     <i data-lucide="menu" class="w-7 h-7 sm:w-8 sm:h-8"></i>
                 </button>
            </div>
        </div>
    </header>

    <div id="mobile-menu" class="fixed inset-0 bg-white/80 dark:bg-black/80 backdrop-blur-xl z-[100] flex-col items-center justify-center space-y-8 text-2xl text-center hidden" role="dialog" aria-modal="true">
        <a href="#about" class="mobile-link">Perfil</a>
        <a href="#skills" class="mobile-link">Competências</a>
        <a href="#projects" class="mobile-link">Projetos</a>
        <a href="#results" class="mobile-link">Resultados</a>
        <a href="#certifications" class="mobile-link">Cursos</a>
        <a href="#contact" class="mobile-link">Contato</a>
    </div>

    <main id="main-content">
        <section id="about" class="min-h-screen flex items-center justify-center text-center relative overflow-hidden py-20 px-4">
            <div class="container mx-auto z-10">
                <div class="max-w-4xl mx-auto glass-effect p-4 sm:p-6 md:p-10 rounded-3xl">
                    <div class="flex flex-col md:flex-row items-center gap-6 sm:gap-8">
                        <div class="md:w-1/3">
                            <img src="https://i.ibb.co/8DPzTV1n/Imagem-do-Whats-App-de-2025-06-23-s-14-27-25-77448b47.jpg" alt="Foto de Gabriel Alves" class="rounded-full w-32 h-32 sm:w-40 sm:h-40 md:w-48 md:h-48 object-cover border-4 border-amarelo-principal shadow-lg mx-auto" loading="eager">
                        </div>
                        <div class="md:w-2/3 text-center md:text-left">
                            <h1 id="headline" class="text-2xl sm:text-3xl md:text-4xl font-bold text-inherit min-h-[100px] md:min-h-[80px]"></h1>
                            <p class="mt-2 text-sm sm:text-base font-semibold text-amarelo-principal">Estratégias de Baixo Custo, Otimização de Processos e Eficiência Operacional</p>
                            <p class="mt-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">
                                Especialista em automação e soluções digitais com mais de 5 anos de experiência. Foco em <strong class="text-gray-800 dark:text-gray-300">redução de custos</strong>, <strong class="text-gray-800 dark:text-gray-300">aumento de vendas</strong> e <strong class="text-gray-800 dark:text-gray-300">eficiência operacional</strong>. Domínio em liderança técnica, metodologias ágeis e análise de dados.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section id="skills" class="py-16 sm:py-20 px-4">
            <div class="container mx-auto">
                <h2 class="section-title">Principais Competências</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8 max-w-6xl mx-auto">
                    <div class="glass-effect p-6 rounded-2xl interactive-card">
                        <i data-lucide="zap" class="w-10 h-10 text-amarelo-principal mb-4 card-icon"></i>
                        <h3 class="card-title">Desenvolvimento & Automação</h3>
                        <p class="card-text">Python, JavaScript, HTML/CSS, Google Apps Script, APIs RESTful, RPA (Conceitual).</p>
                    </div>
                    <div class="glass-effect p-6 rounded-2xl interactive-card">
                        <i data-lucide="package" class="w-10 h-10 text-amarelo-principal mb-4 card-icon"></i>
                        <h3 class="card-title">Plataformas & Ferramentas</h3>
                        <p class="card-text">WordPress, WooCommerce, Excel/Sheets, Trello/Jira, Adobe PS/AE.</p>
                    </div>
                    <div class="glass-effect p-6 rounded-2xl interactive-card">
                        <i data-lucide="trending-up" class="w-10 h-10 text-amarelo-principal mb-4 card-icon"></i>
                        <h3 class="card-title">Marketing Digital & Análise</h3>
                        <p class="card-text">SEO, Google Analytics (GA4), Mídias Sociais, E-mail Marketing, Funis de Venda.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="projects" class="py-16 sm:py-20 px-4">
            <div class="container mx-auto">
                <h2 class="section-title">Experiência e Projetos</h2>
                <p class="text-center text-gray-600 dark:text-gray-400 -mt-8 mb-12 max-w-2xl mx-auto">Atuando como <strong class="text-gray-800 dark:text-gray-300">Desenvolvedor de Automação e Soluções Digitais | Líder de Projetos</strong> (Freelancer, 2019-Atual).</p>
                <div class="grid lg:grid-cols-2 gap-6 sm:gap-8 max-w-6xl mx-auto">
                    
                    <article class="glass-effect p-6 md:p-8 rounded-2xl flex flex-col interactive-card">
                        <div class="flex-grow">
                            <h3 class="card-title mb-4 flex items-center gap-3"><i data-lucide="gas-pump" class="w-6 h-6"></i>Sistema de Notificação</h3>
                            <p class="card-text mb-2"><strong class="card-subtitle">Desafio:</strong> Processos de notificação manuais, lentos e com alto custo operacional no Posto Ipiranga/PR.</p>
                            <p class="card-text mb-2"><strong class="card-subtitle">Solução:</strong> Desenvolvi um sistema de automação completo com Google Apps Script e APIs (Gmail, Sheets, Calendar).</p>
                            <p class="card-text mb-4"><strong class="card-subtitle">Impacto:</strong> Redução drástica de 90% nos custos operacionais.</p>
                        </div>
                        <div class="mt-6 flex gap-4">
                            <a href="#" class="cta-button-primary">Ver Case Study</a>
                        </div>
                    </article>

                    <article class="glass-effect p-6 md:p-8 rounded-2xl flex flex-col interactive-card">
                        <div class="flex-grow">
                            <h3 class="card-title mb-4 flex items-center gap-3"><i data-lucide="shopping-cart" class="w-6 h-6"></i>Revitalização E-commerce</h3>
                            <p class="card-text mb-2"><strong class="card-subtitle">Desafio:</strong> Baixas taxas de conversão e vendas estagnadas na Brazil Tribal.</p>
                            <p class="card-text mb-2"><strong class="card-subtitle">Solução:</strong> Realizei um redesign do UX/UI da loja em WordPress/WooCommerce e otimizei o SEO.</p>
                            <p class="card-text mb-4"><strong class="card-subtitle">Impacto:</strong> Aumento de 18% nas vendas, de R$15 mil para R$17.7 mil/mês.</p>
                        </div>
                         <div class="mt-6 flex flex-wrap gap-4">
                            <a href="#" class="cta-button-primary">Ver Projeto</a>
                            <a href="#" class="cta-button-secondary">Ver Código</a>
                        </div>
                    </article>

                </div>
            </div>
        </section>

        <section id="results" class="py-16 sm:py-20 px-4">
            <div class="container mx-auto">
                <h2 class="section-title">Principais Resultados</h2>
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-8 max-w-6xl mx-auto text-center">
                    <div class="glass-effect p-4 md:p-6 rounded-2xl flex flex-col justify-center items-center">
                        <p class="counter-up text-4xl sm:text-5xl md:text-6xl font-extrabold text-amarelo-principal" data-value="-90"></p>
                        <p class="mt-2 text-xs sm:text-base text-gray-600 dark:text-gray-400 uppercase leading-tight">Custos Operacionais</p>
                    </div>
                    <div class="glass-effect p-4 md:p-6 rounded-2xl flex flex-col justify-center items-center">
                        <p class="counter-up text-4xl sm:text-5xl md:text-6xl font-extrabold text-amarelo-principal" data-value="25" data-prefix="+"></p>
                        <p class="mt-2 text-xs sm:text-base text-gray-600 dark:text-gray-400 uppercase leading-tight">Vendas (Geek Store)</p>
                    </div>
                    <div class="glass-effect p-4 md:p-6 rounded-2xl flex flex-col justify-center items-center">
                        <p class="counter-up text-4xl sm:text-5xl md:text-6xl font-extrabold text-amarelo-principal" data-value="18" data-prefix="+"></p>
                        <p class="mt-2 text-xs sm:text-base text-gray-600 dark:text-gray-400 uppercase leading-tight">Vendas (B. Tribal)</p>
                    </div>
                    <div class="glass-effect p-4 md:p-6 rounded-2xl flex flex-col justify-center items-center">
                        <p class="counter-up text-4xl sm:text-5xl md:text-6xl font-extrabold text-amarelo-principal" data-value="9"></p>
                        <p class="mt-2 text-xs sm:text-base text-gray-600 dark:text-gray-400 uppercase leading-tight">Conversão de Leads</p>
                    </div>
                </div>
            </div>
        </section>
        
        <section id="certifications" class="py-16 sm:py-20 px-4">
            <div class="container mx-auto">
                <h2 class="section-title">Formação & Certificações</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8 max-w-6xl mx-auto">
                    <div class="glass-effect p-6 rounded-2xl interactive-card flex flex-col">
                        <i data-lucide="graduation-cap" class="w-10 h-10 text-amarelo-principal mb-4 card-icon"></i>
                        <h3 class="card-title flex-grow">Tecnólogo em Informática</h3>
                        <p class="card-text">Jalasoft/Bolívia, 2023</p>
                    </div>
                    <div class="glass-effect p-6 rounded-2xl interactive-card flex flex-col">
                        <i data-lucide="building-2" class="w-10 h-10 text-amarelo-principal mb-4 card-icon"></i>
                        <h3 class="card-title flex-grow">Técnico em Adm. de Empresas</h3>
                        <p class="card-text">U.E. España/Bolívia, 2023</p>
                    </div>
                    <div class="glass-effect p-6 rounded-2xl interactive-card flex flex-col">
                        <i data-lucide="file-badge-2" class="w-10 h-10 text-amarelo-principal mb-4 card-icon"></i>
                        <h3 class="card-title flex-grow">Certificações Complementares</h3>
                        <p class="card-text">Google Dev, Febraban, UMSS, UPB.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <section id="contact" class="py-20 px-4">
            <div class="container mx-auto text-center">
                <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold">Vamos construir algo incrível?</h2>
                <p class="mt-4 text-base md:text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Estou disponível para novos projetos e desafios. Entre em contato e vamos conversar sobre como posso ajudar.</p>
                <a href="https://wa.me/5511981064061?text=Ol%C3%A1%2C%20Gabriel!%20Vi%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar." target="_blank" rel="noopener" class="mt-12 inline-block bg-amarelo-principal text-black font-bold py-3 px-8 sm:py-4 sm:px-10 rounded-full text-base sm:text-xl transition-transform duration-300 hover:scale-105 hover:shadow-lg hover:shadow-yellow-400/20">
                    <span class="flex items-center justify-center gap-2">
                        <i data-lucide="send"></i>
                        <span>Falar no WhatsApp</span>
                    </span>
                </a>
            </div>
        </section>
    </main>

    <footer class="py-10 text-center text-gray-500 dark:text-gray-500 px-4">
        <div class="flex justify-center space-x-6 mb-6">
            <a href="https://www.linkedin.com/in/gabriel-alves-da-cruz-692484223" target="_blank" rel="noopener" aria-label="LinkedIn" class="social-link">
                <i data-lucide="linkedin" class="w-6 h-6"></i>
            </a>
            <a href="https://github.com/skreew" target="_blank" rel="noopener" aria-label="GitHub" class="social-link">
                <i data-lucide="github" class="w-6 h-6"></i>
            </a>
            <a href="mailto:gabrielalveslu@gmail.com" aria-label="Email" class="social-link">
                <i data-lucide="mail" class="w-6 h-6"></i>
            </a>
        </div>
        <div class="flex justify-center space-x-6 mb-4 text-sm">
            <a href="/pages/privacidade.html" class="footer-link">Política de Privacidade</a>
            <a href="/pages/termos.html" class="footer-link">Termos de Uso</a>
        </div>
        <p class="text-sm">&copy; <span id="current-year"></span> Gabriel Alves da Cruz. Todos os direitos reservados.</p>
    </footer>
    
    <script type="module" src="/src/main.js"></script>
</body>
</html>
"""

STYLE_CSS_CONTENT = """
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
    .glass-effect {
        @apply bg-white/50 dark:bg-black/40 backdrop-blur-xl border border-black/10 dark:border-white/10 transition-all duration-300;
    }
    .nav-link {
        @apply text-gray-700 dark:text-gray-200 hover:text-amarelo-principal dark:hover:text-amarelo-principal transition-colors relative;
    }
    .nav-link.active {
        @apply text-amarelo-principal dark:text-amarelo-principal;
    }
    .nav-link.active::after {
        content: '';
        @apply absolute -bottom-1 left-0 w-full h-0.5 bg-amarelo-principal;
    }
    .mobile-link {
        @apply text-gray-800 dark:text-gray-200 text-2xl font-semibold;
    }
    .interactive-card {
        @apply transition-all duration-300;
    }
    .interactive-card:hover { 
        @apply -translate-y-2 shadow-2xl dark:shadow-amarelo-principal/10 border-amarelo-principal/50 dark:border-amarelo-principal/50;
    }
    .interactive-card:hover .card-icon {
        @apply scale-110 -rotate-6;
    }
    .card-icon {
        @apply transition-transform duration-300;
    }
    .cta-button-primary {
        @apply inline-block bg-amarelo-principal text-black font-semibold py-2 px-5 rounded-full text-sm transition-transform hover:scale-105;
    }
    .cta-button-secondary {
        @apply inline-block border border-gray-400 dark:border-gray-600 text-gray-600 dark:text-gray-300 font-semibold py-2 px-5 rounded-full text-sm transition-colors hover:bg-gray-200 dark:hover:bg-gray-800 hover:text-gray-800 dark:hover:text-white;
    }
    .skip-link {
        @apply absolute -left-full top-auto w-px h-px overflow-hidden;
    }
    .skip-link:focus, .skip-link:active {
        @apply static w-auto h-auto overflow-visible z-50 bg-amarelo-principal text-black p-3 rounded-lg m-3;
    }
    .section-title {
        @apply text-3xl sm:text-4xl md:text-5xl font-bold text-center mb-12;
    }
    .card-title {
        @apply text-lg sm:text-xl font-bold mb-2;
    }
    .card-subtitle {
       @apply font-semibold text-gray-800 dark:text-gray-300;
    }
    .card-text {
        @apply text-gray-600 dark:text-gray-400 text-sm sm:text-base;
    }
    .social-link {
        @apply text-gray-500 dark:text-gray-400 hover:text-amarelo-principal dark:hover:text-amarelo-principal transition-colors;
    }
    .footer-link {
        @apply text-gray-500 dark:text-gray-400 hover:text-amarelo-principal dark:hover:text-amarelo-principal transition-colors;
    }
}

@layer base {
    .typeit-cursor {
        @apply text-amarelo-principal;
        animation: blink 0.5s infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { @apply bg-gray-200 dark:bg-black; }
    ::-webkit-scrollbar-thumb { @apply bg-amarelo-principal rounded-lg; }
}

@media print {
    body {
        background-color: #fff !important;
        color: #000 !important;
        font-family: 'Times New Roman', serif;
    }
    #main-header, #contact, footer, #background-canvas, #theme-toggle, .cta-button-primary, .cta-button-secondary {
        display: none !important;
    }
    section {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .glass-effect {
        background: #f9f9f9 !important;
        border: 1px solid #ccc !important;
        backdrop-filter: none !important;
        box-shadow: none !important;
    }
    a {
        color: #000 !important;
        text-decoration: underline !important;
    }
    h1, h2, h3, p, li {
        color: #000 !important;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
    #background-canvas {
        display: none;
    }
}
"""

MAIN_JS_CONTENT = """
import './style.css';
import { createIcons, Sun, Moon, Menu, X, Linkedin, Github, Mail, Send, GraduationCap, Building2, FileBadge2, Zap, Package, TrendingUp, GasPump, ShoppingCart } from 'lucide';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import TypeIt from "typeit";
import setupBackground from './components/background.js';

document.addEventListener('DOMContentLoaded', () => {
  try {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // --- SETUP INICIAL ---
    gsap.registerPlugin(ScrollTrigger);
    createIcons({
      icons: { Sun, Moon, Menu, X, Linkedin, Github, Mail, Send, GraduationCap, Building2, FileBadge2, Zap, Package, TrendingUp, GasPump, ShoppingCart }
    });
    document.getElementById('current-year').textContent = new Date().getFullYear();
    setupBackground(document.getElementById('background-canvas'));

    // --- LÓGICA DE TEMA (LIGHT/DARK MODE) ---
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    
    const applyTheme = (theme) => {
      if (theme === 'dark') {
        document.documentElement.classList.add('dark');
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
      } else {
        document.documentElement.classList.remove('dark');
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
      }
    };

    const userPreference = localStorage.getItem('theme');
    const systemPreference = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    const currentTheme = userPreference || systemPreference;
    applyTheme(currentTheme);

    themeToggle.addEventListener('click', () => {
      const newTheme = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
      localStorage.setItem('theme', newTheme);
      applyTheme(newTheme);
    });

    // --- MENU MOBILE ---
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const toggleMenu = (isOpen) => {
      const isNowOpen = typeof isOpen === 'boolean' ? isOpen : mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden', !isNowOpen);
      mobileMenu.classList.toggle('flex', isNowOpen);
      hamburgerBtn.setAttribute('aria-expanded', String(isNowOpen));
      
      if(isNowOpen) {
        hamburgerBtn.setAttribute('aria-label', 'Fechar menu');
        hamburgerBtn.innerHTML = `<i data-lucide="x" class="w-7 h-7 sm:w-8 sm:h-8"></i>`;
      } else {
        hamburgerBtn.setAttribute('aria-label', 'Abrir menu');
        hamburgerBtn.innerHTML = `<i data-lucide="menu" class="w-7 h-7 sm:w-8 sm:h-8"></i>`;
      }
      createIcons({ icons: { Menu, X }});
      if (!isNowOpen) hamburgerBtn.focus();
    };
    hamburgerBtn.addEventListener('click', (e) => { e.stopPropagation(); toggleMenu(); });
    document.querySelectorAll('.mobile-link').forEach(link => link.addEventListener('click', () => toggleMenu(false)));
    document.addEventListener('click', (e) => {
      if (!mobileMenu.classList.contains('hidden') && !mobileMenu.contains(e.target) && !hamburgerBtn.contains(e.target)) {
        toggleMenu(false);
      }
    });

    // --- LÓGICA DE ANIMAÇÕES ---
    const headlineElement = document.getElementById('headline');
    const headlineText = "Especialista em Automação e Soluções Digitais";

    if (headlineElement && !prefersReducedMotion) {
        new TypeIt(headlineElement, {
            strings: headlineText, speed: 50, waitUntilVisible: true, cursorChar: "_", cursorClass: "typeit-cursor"
        }).go();
    } else if (headlineElement) {
        headlineElement.textContent = headlineText;
    }

    if (!prefersReducedMotion) {
      gsap.from("#main-header", { y: -100, opacity: 0, duration: 1, ease: 'power3.out', delay: 0.5 });
      gsap.utils.toArray('section h2, .glass-effect, #about p').forEach(elem => {
        gsap.from(elem, {
          opacity: 0, y: 50, duration: 0.8, ease: 'power3.out',
          scrollTrigger: { trigger: elem, start: 'top 85%', toggleActions: 'play none none none', once: true }
        });
      });

      gsap.utils.toArray(".counter-up").forEach(elem => {
        const endValue = parseInt(elem.dataset.value, 10);
        const prefix = elem.dataset.prefix || '';
        const suffix = elem.dataset.value.includes('90') ? '%' : elem.dataset.value.includes('18') ? '%' : elem.dataset.value.includes('25') ? '%' : '%';
        gsap.to({ val: 0 }, {
          val: endValue, duration: 2, ease: "power1.out",
          scrollTrigger: { trigger: elem, start: "top 85%", once: true },
          onUpdate: function() { elem.textContent = prefix + Math.ceil(this.targets()[0].val) + suffix; }
        });
      });
    } else {
        gsap.utils.toArray(".counter-up").forEach(elem => {
            const endValue = parseInt(elem.dataset.value, 10);
            const prefix = elem.dataset.prefix || '';
            const suffix = elem.dataset.value.includes('90') ? '%' : elem.dataset.value.includes('18') ? '%' : elem.dataset.value.includes('25') ? '%' : '%';
            elem.textContent = prefix + endValue + suffix;
        });
    }

    gsap.utils.toArray("#main-nav a").forEach(link => {
      const section = document.querySelector(link.getAttribute("href"));
      if (section) {
        ScrollTrigger.create({
          trigger: section, start: "top center", end: "bottom center",
          onToggle: self => {
            document.querySelectorAll("#main-nav a").forEach(l => l.classList.remove("active"));
            if (self.isActive) link.classList.add("active");
          }
        });
      }
    });

  } catch (error) {
    console.error("Erro ao inicializar o script do site:", error);
  }
});
"""

BACKGROUND_JS_CONTENT = """
export default function setupBackground(canvas) {
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let particles = [];
    
    const resizeCanvas = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    };

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 1.5 + 1;
            this.speedX = (Math.random() * 0.4 - 0.2);
            this.speedY = (Math.random() * 0.4 - 0.2);
            this.colorLight = 'rgba(245, 158, 11, 0.6)'; // amarelo-secundario
            this.colorDark = 'rgba(255, 215, 0, 0.5)'; // amarelo-principal
        }
        update() {
            if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
            if (this.y > canvas.height || this.y < 0) this.speedY *= -1;
            this.x += this.speedX;
            this.y += this.speedY;
        }
        draw() {
            const isDarkMode = document.documentElement.classList.contains('dark');
            ctx.fillStyle = isDarkMode ? this.colorDark : this.colorLight;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function init() {
        particles = [];
        let numberOfParticles = (canvas.height * canvas.width) / 12000;
        for (let i = 0; i < numberOfParticles; i++) {
            particles.push(new Particle());
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animate);
    }

    window.addEventListener('resize', () => {
        resizeCanvas();
        init();
    });

    resizeCanvas();
    init();
    
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        animate();
    }
}
"""

README_MD_CONTENT = """
# Portfólio Profissional - Gabriel Alves da Cruz

Este é o código-fonte do meu portfólio profissional, construído com tecnologias web modernas para garantir performance, organização e uma ótima experiência de usuário.

**[Acesse a versão ao vivo aqui](https://skreew.github.io/gcruz/)**

## ✨ Funcionalidades

- **Design Totalmente Responsivo:** Adaptado para uma visualização perfeita em desktops, tablets e celulares.
- **Light/Dark Mode:** Alternância de tema com salvamento da preferência do usuário.
- **Animações Modernas:** Interações sutis e animações de scroll que melhoram a experiência, com suporte a `prefers-reduced-motion` para acessibilidade.
- **Estrutura Profissional:** Organização de arquivos e gerenciamento de dependências com Vite e NPM.
- **Otimizado para Performance:** Geração de arquivos CSS e JS otimizados para um carregamento rápido.

## 🛠️ Tecnologias Utilizadas

- **Vite:** Ferramenta de build para um desenvolvimento rápido e moderno.
- **Tailwind CSS:** Framework CSS utility-first para estilização rápida e responsiva.
- **JavaScript (ES6+):** Para toda a interatividade do site.
- **GSAP (GreenSock Animation Platform):** Para animações de scroll complexas e performáticas.
- **TypeIt.js:** Para a animação de digitação no título.
- **Lucide Icons:** Biblioteca de ícones SVG leve e customizável.

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
- [Node.js](https://nodejs.org/) (versão 18 ou superior)
- [npm](https://www.npmjs.com/) (geralmente vem com o Node.js)

### Passos

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/skreew/gcruz.git](https://github.com/skreew/gcruz.git)
   cd gcruz
   ```
2. **Instale as dependências:**
   ```bash
   npm install
   ```
3. **Inicie o servidor de desenvolvimento:**
   ```bash
   npm run dev
   ```

   Abra [http://localhost:5173](http://localhost:5173) (ou o endereço que aparecer no seu terminal) para ver o projeto.
"""

def criar_estrutura_do_projeto(diretorio_raiz):
    """
    Cria a estrutura completa de pastas e arquivos para o projeto do portfólio.
    """
    print(f"A criar a estrutura do projeto em: '{diretorio_raiz}/'")

    # Dicionário que mapeia o caminho do arquivo para a sua variável de conteúdo
    arquivos_a_criar = {
        "package.json": PACKAGE_JSON_CONTENT,
        "tailwind.config.js": TAILWIND_CONFIG_JS_CONTENT,
        "postcss.config.js": POSTCSS_CONFIG_JS_CONTENT,
        ".gitignore": GITIGNORE_CONTENT,
        "index.html": INDEX_HTML_CONTENT,
        "README.md": README_MD_CONTENT,
        "src/style.css": STYLE_CSS_CONTENT,
        "src/main.js": MAIN_JS_CONTENT,
        "src/components/background.js": BACKGROUND_JS_CONTENT
    }

    # Garante que o diretório raiz do projeto existe
    os.makedirs(diretorio_raiz, exist_ok=True)

    # Itera sobre o dicionário para criar cada arquivo
    for caminho_arquivo, conteudo in arquivos_a_criar.items():
        # Constrói o caminho completo para o arquivo
        caminho_completo = os.path.join(diretorio_raiz, caminho_arquivo)
        
        # Cria as pastas necessárias para o arquivo (ex: 'src/components/')
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        
        # Escreve o conteúdo no arquivo
        try:
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                # textwrap.dedent remove a indentação comum do início das linhas da string
                f.write(textwrap.dedent(conteudo).strip())
            print(f"  -> Arquivo criado com sucesso: {caminho_arquivo}")
        except IOError as e:
            print(f"  -> ERRO ao criar o arquivo {caminho_arquivo}: {e}")
            
    # Cria pastas vazias adicionais, se necessário
    try:
        os.makedirs(os.path.join(diretorio_raiz, "pages"), exist_ok=True)
        print(f"  -> Diretório criado com sucesso: pages/")
    except OSError as e:
        print(f"  -> ERRO ao criar o diretório 'pages': {e}")


    print("\n-------------------------------------------------")
    print("Estrutura do projeto criada com sucesso!")
    print("Para iniciar, siga os seguintes passos no seu terminal:")
    print(f"1. Entre na pasta do projeto: cd {diretorio_raiz}")
    print("2. Instale as dependências do Node.js: npm install")
    print("3. Inicie o servidor de desenvolvimento: npm run dev")
    print("-------------------------------------------------")


# --- PONTO DE ENTRADA DO SCRIPT ---
# Este bloco só será executado quando o script for chamado diretamente
if __name__ == "__main__":
    NOME_DO_PROJETO = "portfolio-gabriel-alves"
    criar_estrutura_do_projeto(NOME_DO_PROJETO)
