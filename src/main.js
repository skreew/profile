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