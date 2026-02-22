# Edu-VixenAK - Educational AI Assistant Platform

## Overview

Edu-VixenAK is a comprehensive educational platform that combines AI-powered tools with traditional teaching workflows. The system provides educators with intelligent assistants for creating papers, quizzes, managing students, and generating educational content. Built as a full-stack application with React frontend and Node.js/Express backend, it leverages AI capabilities through Google's Gemini API for content generation and educational assistance.

## User Preferences

Preferred communication style: Simple, everyday language.
Color scheme preference: Sophisticated dark theme with subtle colors - no overwhelming neon effects, no plain white backgrounds. Prefers slate/blue color palette with elegant subtle accents.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite for fast development and optimized production builds
- **UI Framework**: Tailwind CSS with shadcn/ui components
- **State Management**: TanStack Query (React Query) for server state management
- **Routing**: Wouter for lightweight client-side routing
- **Styling**: Sophisticated dark theme with slate/blue color palette and subtle accent colors

### Backend Architecture
- **Runtime**: Node.js with Express.js framework
- **Language**: TypeScript with ES modules
- **Database**: PostgreSQL with Drizzle ORM
- **Database Provider**: Neon Database (serverless PostgreSQL)
- **Session Management**: connect-pg-simple for PostgreSQL session storage
- **AI Integration**: Google Gemini API for content generation and chat functionality

### Project Structure
```
├── client/          # React frontend application
├── server/          # Express.js backend server
├── shared/          # Shared TypeScript schemas and types
├── migrations/      # Database migration files
└── dist/           # Production build output
```

## Key Components

### AI-Powered Educational Tools
1. **Paper Maker**: Generates customized question papers based on subject, grade, and requirements
2. **Quiz Generator**: Creates interactive quizzes with multiple question types and Google Forms-like sharing functionality
3. **Paper Checker**: Automated grading and evaluation system
4. **Mind Map Generator**: Creates visual concept maps for topics
5. **Flash Cards**: Generates study cards for memorization
6. **Presentation Generator**: Creates educational slide presentations
7. **Message Creator**: Generates formal communications and announcements
8. **Illustration Studio**: AI-powered image generation for educational content
9. **Play Cards**: Gamified learning through interactive card games
10. **Timetable Generator**: AI-powered timetable creation with interactive editing and database persistence

### Quiz Sharing System
- **Share Links**: Teachers can generate shareable links for quizzes that students can access without accounts
- **Online Quiz Taking**: Students can take quizzes through a clean, distraction-free interface
- **Automatic Scoring**: Real-time grading with detailed feedback and results
- **Teacher Dashboard**: View student submissions, scores, and statistics
- **Progress Tracking**: Monitor student performance and quiz completion rates

### Core Management Systems
- **Student Records**: Complete student information management
- **Project Folder**: File organization and storage system
- **Admin Assistant**: Administrative task automation
- **AI Chat Assistant**: Real-time educational support

### User Interface Components
- **Responsive Design**: Mobile-first approach with desktop optimization
- **Dark Theme**: Sophisticated slate-based dark theme with subtle color accents
- **Navigation**: Bottom navigation for mobile, sidebar for desktop
- **Search**: Intelligent search across all content types
- **Modular Tools**: Component-based architecture for easy maintenance

## Data Flow

### Authentication & User Management
- Default user system with role-based access (teacher/admin)
- Session-based authentication using PostgreSQL storage
- User profiles with institutional information and preferences

### Content Generation Flow
1. User selects AI tool and provides parameters
2. Frontend validates input and sends request to backend
3. Backend processes request and calls appropriate Gemini API endpoint
4. AI generates structured content based on educational requirements
5. Backend validates and stores generated content in database
6. Frontend displays results with editing and export capabilities

### Data Persistence
- All generated content (papers, quizzes, projects) stored in PostgreSQL
- Quiz sharing system with public links and submission tracking
- Student quiz submissions stored with detailed scoring and feedback
- File uploads handled through project folder system
- Search indexing across all content types for quick retrieval
- Real-time updates using TanStack Query for optimal user experience

## External Dependencies

### AI Services
- **Google Gemini API**: Primary AI service for content generation, chat, and educational assistance
- **API Models**: Uses both Gemini 2.5 Flash and Gemini 2.5 Pro based on complexity requirements

### Database & Storage
- **Neon Database**: Serverless PostgreSQL for production deployment
- **Drizzle ORM**: Type-safe database operations with automatic migrations
- **Session Storage**: PostgreSQL-backed session management

### UI & Styling
- **Radix UI**: Accessible, unstyled UI components
- **Tailwind CSS**: Utility-first CSS framework
- **Custom Design System**: Sophisticated slate color palette with elegant styling

### Development Tools
- **Vite**: Fast build tool with HMR support
- **TypeScript**: Type safety across frontend and backend
- **ESBuild**: Fast bundling for production deployment

## Deployment Strategy

### Development Environment
- **Local Development**: Vite dev server with Express backend
- **Hot Module Replacement**: Real-time updates during development
- **Environment Variables**: Separate configuration for development and production

### Production Build
- **Frontend**: Vite builds to `dist/public` directory
- **Backend**: ESBuild bundles server code to `dist/index.js`
- **Static Serving**: Express serves built frontend in production
- **Database**: Drizzle handles schema migrations automatically

### Replit Integration
- **Replit-specific plugins**: Cartographer for development enhancement
- **Runtime error handling**: Custom error overlay for development
- **Environment detection**: Automatic configuration based on Replit environment

### Configuration Management
- **Environment Variables**: DATABASE_URL, GEMINI_API_KEY, NODE_ENV
- **Database Migrations**: Automatic schema updates via Drizzle Kit
- **Build Scripts**: Unified build process for frontend and backend

The system is designed for scalability with its modular architecture, allowing for easy addition of new AI tools and educational features while maintaining consistent user experience across all components.

## Recent Updates (July 26, 2025)
- **STUNNING ORBITAL DASHBOARD WITH SIDEBAR COMPLETE**: Enhanced the orbital dashboard with central "Explore Tools" card and comprehensive navigation sidebar
  - **Central Explore Tools Card**: Spectacular glowing central hub with rocket icon, pulsing animations, and holographic rings
  - **Collapsible Sidebar**: Sophisticated slide-in navigation with Home, Profile, Feedback sections, and tool shortcuts
  - **Admin Features**: Conditional admin-only "View Feedback" option in sidebar navigation
  - **Smooth Animations**: Spring-powered sidebar transitions, hover effects, and glow interactions
  - **Complete Tool Integration**: All 10 tools accessible both via orbital motion and sidebar quick access
  - **Neon Aesthetic**: Consistent glowing theme across sidebar and main dashboard with custom scrollbars
  - **Mobile Responsive**: Sidebar overlay design that doesn't interfere with orbital layout on any screen size
  - **Performance Optimized**: Efficient animation system with proper component protection and error handling
- **ULTRA-MODERN ORBITAL DASHBOARD COMPLETE**: Implemented jaw-dropping futuristic main dashboard with orbital motion and spectacular visual effects
  - **Orbital Motion System**: 10 AI tools float in continuous orbital motion around central glowing core with pause-on-hover functionality
  - **Deep Space Background**: Galaxy-style gradient with animated particles, data waves, and floating holographic elements
  - **Interactive Tool Cards**: Glassmorphism cards with 3D hover effects, spotlight glow, and smooth orbital positioning
  - **Responsive Design**: Orbital motion seamlessly transitions to mobile grid layout with preserved visual effects
  - **Advanced Animations**: Framer Motion-powered 360° rotations, levitation effects, and holographic surface reflections
  - **Futuristic Typography**: Orbitron and Exo 2 fonts with neon outlines and gradient text effects
  - **Protection System**: Built-in component protection monitor prevents auto-deletion and preserves all tool references
  - **Performance Optimized**: Smooth 60fps animations with efficient rendering and mobile-first responsive breakpoints
- **COMPREHENSIVE MULTI-STRATEGY VISUAL ASSISTANT COMPLETE**: Implemented full multi-source educational content discovery system
  - **5-Strategy Pipeline**: Wikimedia Commons → DALL-E → Pixabay → Visual Mind AI → Educational Placeholders
  - **Smart Query Detection**: Distinguishes between simple subjects (orange, apple) and complex scientific queries for appropriate search strategies
  - **DALL-E Integration**: Complete AI image generation with educational prompt engineering for custom diagrams
  - **Pixabay Integration**: Educational image search with filtering for academic relevance and illustration priority
  - **Visual Mind AI Ready**: Framework prepared for mind map generation (implementation placeholder for future API)
  - **Enhanced Wikimedia Integration**: Improved educational content filtering with scientific terms, SVG diagram prioritization, and metadata extraction
  - **Balanced Relevance Scoring**: Lower thresholds for simple subjects, strict scientific filtering for complex educational topics
  - **Comprehensive Fallback System**: Graceful degradation through all strategies ensuring content is always found
  - **API Key Management**: Proper environment variable handling with graceful failures when keys are missing
- **SMART VISUAL ASSISTANT DEBUGGING & OPTIMIZATION COMPLETE**: Implemented comprehensive debugging system and resolved image relevance issues
  - **Complete Data Flow Logging**: Added detailed logs at every step from input to external API to final output
  - **Enhanced Educational Filtering**: Implemented strict filtering that rejects generic content and requires educational relevance
  - **Multiple Search Strategy**: System now performs 3 different searches with scientific keywords to increase relevance
  - **Intelligent Fallback System**: When no educational images found, prioritizes textual diagrams over irrelevant stock photos
  - **Scientific Term Detection**: Analyzes queries for scientific content and adjusts search approach accordingly
  - **Debugging Guide Created**: Complete DEBUGGING_GUIDE.md with step-by-step troubleshooting for developers
  - **Result Prioritization**: Educational diagrams get higher priority when stock images lack educational value
- **SMART VISUAL ASSISTANT MODULE IMPLEMENTED**: Successfully created comprehensive intelligent visual content discovery tool for educational materials
  - **New Tool Added**: Smart Visual Assistant added to both dashboard and sidebar navigation with purple/cyan theme
  - **Dedicated API Endpoint**: Created `/api/visual-assistant/find-image` endpoint for module integration with consistent JSON response format
  - **Visual Assistant Service**: Built robust service class with Unsplash integration, educational content filtering, and error handling
  - **Presentation Integration**: Updated presentation generator to use Visual Assistant for automatic image discovery on diagram slides
  - **Educational Focus**: Advanced filtering system that prioritizes educational content and rejects non-academic images
  - **Image Replace Modal**: Created user override component allowing teachers to replace AI-selected images with custom alternatives
  - **Secure API Management**: Proper environment variable handling for external API keys with graceful fallbacks
- **EDUCATIONAL TEXTUAL DIAGRAM SYSTEM FINALIZED**: Successfully streamlined presentation generator to focus exclusively on high-quality educational diagrams
  - **Unsplash Integration Disabled**: Removed per user request due to generic image quality issues
  - **Always-On Diagrams**: Educational textual diagrams are now automatically included in all relevant presentations
  - **Simplified UI**: Removed "Include Diagrams" checkbox option for cleaner, streamlined interface
  - **Comprehensive Coverage**: Added physics diagrams (refraction, reflection, light waves) alongside existing biology and chemistry templates
  - **Enhanced Physics Templates**: Snell's Law, Law of Reflection, electromagnetic wave properties with proper formulas
  - **Educational Priority**: Focus exclusively on accurate scientific content over unpredictable visual elements
- **PROJECT EMAIL INTEGRATION COMPLETE**: Successfully integrated dedicated project email address into feedback system
  - **Project Email**: edu.vixenak@gmail.com configured for user feedback and support
  - **Dual Contact Methods**: Users can submit feedback via web form or email directly
  - **Professional Contact**: Feedback form displays dedicated project email for direct communication
  - **Email Setup Documentation**: Created EMAIL_SETUP.md with complete setup guide and best practices

## Previous Updates (July 23, 2025)
- **CROSS-PLATFORM PWA IMPLEMENTATION COMPLETE**: Successfully implemented comprehensive Progressive Web App functionality for universal device compatibility
  - **PWA Manifest & Service Worker**: Complete PWA setup with offline caching, app-like installation on all devices
  - **Universal Install Experience**: Smart install prompts work on mobile (iOS Safari, Android Chrome) and desktop (Chrome, Edge, Firefox, Safari)
  - **Cross-Platform Guide Component**: Interactive installation guide with device-specific instructions for mobile and desktop
  - **Offline Functionality**: Service worker enables offline access to cached content and faster loading times
  - **App-Like Experience**: Standalone mode, custom icons, splash screens, and native-like navigation
  - **Browser Compatibility**: Full support for Chrome 67+, Firefox 60+, Safari 11.1+, Edge 79+ with graceful fallbacks
- **AUTHENTICATION FULLY RESTORED**: Fixed authentication routes to properly use memory storage interface instead of direct database queries
  - **Login/Registration Working**: Both endpoints now successfully use storage.getUserByEmail() and storage.createUser() methods
  - **API Confirmed Working**: Multiple test accounts created and authenticated successfully via API calls
  - **Memory Storage Integration**: Seamless integration between authentication routes and memory storage fallback system
  - **Production-Ready Fallback**: Complete authentication flow with proper bcrypt hashing, JWT tokens, and session management
  - **Test Credentials**: Kate.cute.rida@gmail.com / Test123!@# confirmed working, plus new user registration functional

## Recent Updates (July 23, 2025)
- **COMPREHENSIVE FEEDBACK SYSTEM COMPLETE**: Successfully implemented secure feedback collection, storage, and management with AI-powered analysis
  - **Secure Data Collection**: Enhanced feedback API with input sanitization, IP tracking, rate limiting (5 submissions per 15 minutes), and JWT user authentication
  - **Advanced Security Schema**: Updated database schema with security indexes, attachment URL storage, IP address logging, and enhanced browser fingerprinting
  - **AI-Powered Analysis**: Integrated Gemini AI for sentiment analysis, priority suggestions, keyword extraction, and category classification
  - **Admin Dashboard**: Built comprehensive feedback management interface with filtering, status updates, priority management, and real-time statistics
  - **Cloud Storage Ready**: Prepared secure file attachment system with validation and cloud storage integration (AWS S3/Google Cloud)
  - **Rate Limiting & Monitoring**: Implemented abuse prevention with detailed logging and security monitoring capabilities
  - **Professional UI/UX**: Prominent feedback buttons in sidebar and dashboard header with structured form design and auto-closure confirmation
- **MAJOR ENHANCEMENT - Essential Security Features System**: Implemented comprehensive security management with professional profile picture handling, 2FA setup, and secure account deletion
  - **Profile Picture Upload**: Professional avatar system with 5MB file limit, image format validation, and default initials fallback
  - **Two-Factor Authentication (2FA)**: Complete 2FA setup flow with QR code generation, authenticator app integration (Google/Authy/Microsoft), manual secret key backup, and disable functionality
  - **Account Deletion**: Secure deletion process with typed confirmation requirement, comprehensive data deletion explanation, and proper cleanup of user data
  - **Security Dashboard**: Organized into Password & Login Security, 2FA Management, Session Management, and Danger Zone sections
  - **Session Management**: Logout from all other devices while preserving current session, and complete logout from all devices functionality
  - **Professional Security UI**: Clear explanations of security features, color-coded status indicators, and non-technical language for user-friendly security management
  - **Database Schema Enhancement**: Added twoFactorEnabled and twoFactorSecret fields with proper backend API endpoints for all security operations
- **MAJOR ENHANCEMENT - Complete App Preferences & Notifications System**: Implemented comprehensive user preference management with sophisticated notification controls
  - **Notification Management**: 5 distinct notification types with granular toggle controls (Email Alerts, Content Generation, General Updates, Master Email, Master In-App)
  - **Smart Notification Settings**: Classroom insights alerts, content completion notifications, and general platform announcements with descriptive tooltips
  - **Language Preferences**: 10 language options (English, Spanish, French, German, Chinese, Japanese, Korean, Portuguese, Italian, Russian) affecting AI content and interface
  - **Communication Preferences**: Choice between Email, In-App Messages, or Both for critical communications with visual radio-style selection
  - **Master Toggle Controls**: Separate master switches for email and in-app notifications with color-coded visual feedback
  - **Professional UI Design**: Organized into logical card sections with clear descriptions, helpful tooltips, and consistent visual hierarchy
  - **Auto-save Integration**: Preferences automatically save with existing profile auto-save system and manual save button
- **MAJOR ENHANCEMENT - Secure User Authentication System**: Implemented comprehensive registration with advanced security features
  - **Password Security**: Added bcrypt hashing with 12 salt rounds for secure password storage
  - **Real-time Validation**: Password requirements displayed with live feedback (8+ chars, uppercase, lowercase, number, special character)
  - **Form Validation**: Comprehensive client and server-side validation for all fields
  - **Show/Hide Password**: Toggle buttons for both password and confirm password fields
  - **User-Friendly Errors**: Clear, actionable error messages for validation failures
  - **Optional Authentication**: Users can access all tools without accounts, registration available for progress saving
  - **Professional UI**: Modern registration form with institutional field and terms acceptance
- **MAJOR ENHANCEMENT - Comprehensive Excel Export System**: Implemented professional Excel export functionality using XLSX library
  - **Real Excel Files**: Creates actual .xlsx files (not CSV) with proper formatting and multiple worksheets
  - **Gradebook Sheet**: Complete student data with grades, percentages, letter grades, and pass/fail status
  - **Class Info Sheet**: Summary with class details, grading scale, and export metadata
  - **Dynamic Columns**: Automatically adjusts for any number of assignment categories
  - **Professional Formatting**: Proper column widths, clear headers, and organized data structure
  - **File Naming**: Smart file naming with class name and export date for easy organization
  - **User-Friendly Interface**: Added neon-green "Export to Excel" button in gradebook header
- **MAJOR ENHANCEMENT - Advanced Attendance Management with Date Range Analytics**: Enhanced attendance system with comprehensive statistics and date-based filtering
  - **Date Range Selection**: Added "From Date" to "To Date" selectors for flexible attendance period analysis
  - **Total Lectures Calculation**: Smart calculation of total lectures based on selected date range (3 lectures per week assumption)
  - **Class Average Display**: Real-time calculation and display of overall class attendance percentage
  - **Enhanced Attendance Table**: Added "Attended/Total" column showing detailed lecture count breakdown
  - **Visual Statistics Panel**: Professional card-based overview with color-coded attendance metrics
  - **Individual Student Tracking**: Each student shows attended lectures vs total lectures with percentage breakdown
  - **Numerical Attendance Display**: Attendance status now shows clear numerical format (e.g., "50/65") with attended/total lectures
  - **Detailed Breakdown Column**: Added comprehensive breakdown showing Present, Late, Excused, and Absent counts for each student
  - **Simplified Table Design**: Removed daily attendance status column, focusing on overall attendance numbers and detailed breakdown
- **MAJOR FEATURE REPLACEMENT - Groups → Attendance Management System**: Successfully replaced Groups functionality with comprehensive attendance tracking
  - **Database Schema**: Added `attendance` and `attendanceSummary` tables with proper foreign key relationships
  - **Backend API**: Created 3 new endpoints: GET/POST attendance records, GET attendance summaries, helper function for summary updates
  - **Frontend Implementation**: Complete attendance interface with date picker, status dropdowns (Present/Absent/Late/Excused), and summary cards
  - **Real-time Updates**: Attendance records update summary statistics automatically, with proper React Query cache invalidation
  - **Status Tracking**: Four attendance statuses with color-coded UI (Present=green, Absent=red, Late=orange, Excused=blue)
  - **Percentage Calculations**: Automatic attendance percentage calculation considering present+late+excused as acceptable attendance
- **CRITICAL FIX - React Hooks Error Resolution**: Fixed "rendered more hooks than during the previous render" error in StudentRecords component
  - **Root Cause**: Conditional React Query hooks were changing hook count when selectedClass state changed
  - **Solution**: Updated all query keys to use consistent patterns with proper enabled flags
  - **Query Standardization**: Changed from template literals to array-based keys (`['students', selectedClass?.id || 'none']`)
  - **Cache Management**: Updated all mutation invalidation calls to use new key patterns
- **MAJOR ENHANCEMENT - Interactive Editable Analytics Charts**: Implemented fully functional interactive chart system with professional editing capabilities
  - **Real Interactive Charts**: Added proper Recharts library integration with Bar, Pie, Line, and Area chart visualizations
  - **Functional Edit Buttons**: Each chart has working "Edit Data" buttons that open modal dialogs for data modification
  - **4 Chart Types with Full Editing**:
    - **Bar Chart**: Weekly attendance patterns with attendance/target percentages - fully editable
    - **Pie Chart**: Student engagement distribution with participation levels - editable percentages and counts  
    - **Line Chart**: Assignment completion trends over time - editable completion rates, submissions, and on-time percentages
    - **Area Chart**: Daily activity intensity with lecture/discussion levels - fully editable time-based data
  - **Professional Edit Dialogs**: Each chart type has dedicated modal with input fields for all data points
  - **Real-time Updates**: Charts update immediately when data is changed through edit dialogs
  - **Toast Notifications**: Success messages when chart data is saved
  - **Dark Theme Integration**: All charts use sophisticated dark theme with neon color accents
  - **Responsive Design**: Charts adapt to screen size with proper tooltips, legends, and hover effects
- **Navigation Synchronization Complete**: Resolved confusion between different versions of Classroom Management tool
  - **Removed Duplicate Component**: Deleted old `components/tools/student-records.tsx` file that was causing version conflicts
  - **Unified Navigation**: Both dashboard and sidebar now use identical comprehensive StudentRecords page component
  - **URL Parameter Fix**: Updated home.tsx to redirect `/?tool=student-records` to proper `/student-records` route
  - **Single Source of Truth**: All navigation paths now lead to the same full-featured classroom management system
- **Class Deletion Bug Fix**: Resolved database schema mismatch preventing class deletion
  - **Root Cause**: Code attempted to delete from grades table using non-existent `classId` column
  - **Solution**: Fixed cascade deletion to properly delete grades through assignment relationships
  - **Database Operations**: Now correctly deletes grades → assignments → categories → class students → class in proper order
  - **Verification**: Class deletion functionality now works completely and removes all related data safely

## Previous Updates (July 22, 2025)
- **PHASE 29 - COMPREHENSIVE CLASSROOM MANAGEMENT SYSTEM**: Implemented full-featured classroom management with database schema, API routes, and UI
  - **Database Schema**: Added 6 new tables - classes, classStudents, assignmentCategories, assignments, grades, communicationLogs, studentProgress
  - **API Endpoints**: 15+ new routes for CRUD operations, AI analysis, CSV import, and group generation
  - **UI Components**: Complete tabbed interface with Classes, Students, Gradebook, Analytics, and Groups tabs
  - **Student Profiles**: Comprehensive profile system with contact info, emergency contacts, confidential notes, and accommodations
  - **AI Integration**: Progress analysis, intervention suggestions, academic performance alerts, and intelligent group generation
  - **CSV Import**: Bulk student roster import functionality for efficient class setup
- **Tool Rename**: Changed "Student Records" to "Classroom Management & Data" in both dashboard and sidebar to better reflect comprehensive classroom management functionality
- **Tool Cleanup**: Removed Illustration Studio from both dashboard and sidebar navigation, deleted IllustrationStudio.tsx file to streamline tool selection
- **Navigation Synchronization Fix**: Resolved Flash Cards route inconsistency - both dashboard and sidebar now point to same `/flash-cards` route
- **PHASE 28 COMPLETE - Spaced Repetition System (SRS)**: Successfully implemented intelligent SRS with 4-tier recall rating system (again, hard, good, easy)
- **Dashboard Integration**: Added Flash Cards to main dashboard with neon-pink theme and "SRS" status badge for easy access from home page
- **Progressive Scheduling Algorithm**: Advanced intervals - again (5 min), hard (1 day), good (3 days + multiplier), easy (7 days + multiplier) based on success rate
- **Smart Study Sessions**: Cards removed from session after review (except "again" ratings) with automatic session progression
- **PHASE 27 COMPLETE - Flashcard CRUD System**: Successfully implemented comprehensive flashcard editing and deletion functionality with both backend endpoints and frontend integration
- **Backend CRUD Endpoints**: Added PUT /api/flashcards/:id and DELETE /api/flashcards/:id with complete validation and error handling
- **Enhanced CreateFlashcard Component**: Extended to support both creation and editing modes with proper state management and form pre-population
- **Interactive Study Interface**: Enhanced FlashcardStudy component with Edit and Delete buttons, confirmation dialogs, and seamless state updates
- **Complete Workflow Integration**: Users can now AI-generate → manually create → study → edit → delete flashcards in a unified experience
- **PHASE 18 COMPLETE - React Flow Integration**: Successfully implemented React Flow-based mind map visualization system
- **Custom Node Components**: Created CustomMindMapNodes.tsx with Handle imports from @xyflow/react for proper node connections
- **MindMapDisplay Component**: Built dedicated component with exact specifications (initialNodes, initialEdges, onGenerateAnother, onSaveMindMap, onExportImage props)
- **ReactFlowProvider Integration**: Proper React Flow context setup with Controls, MiniMap, and Background components
- **Professional Node Styling**: Custom nodes with Tailwind CSS classes, minimum dimensions (150px width, 50px height), proper text centering with flex layout
- **Dagre Layout Algorithm**: Automatic professional positioning with both vertical and horizontal layout options
- **Dual Visualization System**: Users can now switch between SVG view and Flow view tabs within same interface
- **Interactive Features**: Zoom, pan, MiniMap navigation, and layout switching controls
- **Type Safety**: Complete TypeScript interfaces and proper Handle positioning for all node types
- **Custom Node Types**: Central (indigo), Main (colored), Sub (light), Process, Decision, Start/End nodes with distinct styling
- **Navigation Restructure Complete**: Removed bottom navigation bar entirely to create cleaner interface design
- **My Projects Dual Access**: Added My Projects to both dashboard (emerald-colored card) and sidebar tools list for easy access
- **Dashboard Color Restoration**: Fixed dashboard tools to display with vibrant neon colors (cyan, green, purple, blue, orange, emerald)
- **Mind Map Export System**: Implemented comprehensive export functionality with PNG, PDF, and DOC format support

## Previous Updates (July 21, 2025)
- **Phase 15 - Message Creator Enhancement**: Extended DocumentGeneratorForm to support 4 new message types for targeted audience communication
- **Navigation Synchronization**: Resolved major inconsistency where different navigation methods accessed different tool versions
- **Route Consolidation**: Standardized all routes to /tool-name format with consistent redirect mappings across all components

## Previous Updates (July 21, 2025)
- **Document Generator Complete**: Added comprehensive save and export functionality for all document types (application, letter, proposal)
- **Project Integration**: Documents can now be saved directly to My Projects with proper metadata and categorization
- **Word Export**: Implemented DOCX export using docx library with professional formatting and automatic file download
- **Three-Button System**: Copy to clipboard, Save to Projects, and Export as Word options for every generated document
- **Backend API Enhancement**: Added /api/documents/save and /api/documents/export-docx endpoints with full error handling
- **Toast Notifications**: User-friendly success/error feedback for all document operations using shadcn/ui toast system
- **Proposal Writer Integration**: Full proposal generation with 7-section structure accessible through Admin Assistant Dashboard

## Previous Updates (July 17, 2025)
- **Timetable Generator**: Complete implementation with AI-powered generation, interactive editing, and database persistence
- **Database Integration**: Added timetables table with full CRUD operations and PostgreSQL storage
- **API Fix**: Resolved critical API request parameter ordering issue that was preventing timetable generation
- **Data Structure Fix**: Fixed timetable data structure handling to properly extract nested API response data
- **User Interface**: Fully functional timetable editing interface with in-place editing and save functionality
- **Error Handling**: Added comprehensive error boundaries and validation for timetable display components