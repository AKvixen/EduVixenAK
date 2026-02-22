# Visual Diagrams Setup Guide - Edu-VixenAK

## Overview
The Edu-VixenAK platform now includes comprehensive visual diagram integration for educational presentations. This system automatically finds and embeds relevant scientific diagrams from Unsplash's educational image database.

## Required Environment Variables

### UNSPLASH_ACCESS_KEY
To enable visual diagrams in presentations, you need an Unsplash API access key.

**Setup Steps:**
1. Go to [Unsplash Developers](https://unsplash.com/developers)
2. Create a free developer account
3. Create a new application:
   - **Application name**: Edu-VixenAK Educational Platform
   - **Description**: Educational platform for generating presentations with visual diagrams
   - **Use case**: Educational content creation with scientific diagrams
4. Copy your **Access Key** (not the Secret Key)
5. Add to Replit Secrets:
   - **Key**: `UNSPLASH_ACCESS_KEY`
   - **Value**: Your access key from step 4

## Features

### 🔬 Smart Diagram Detection
- AI automatically identifies when scientific diagrams would enhance slides
- Searches for relevant educational images based on slide content
- Supports biology, chemistry, physics, and other scientific topics

### 🖼️ Image Integration
- **Frontend Preview**: Live preview of actual diagrams in slide previews
- **Error Handling**: Graceful fallback when images can't be loaded
- **Professional Attribution**: Automatic photographer credits from Unsplash

### 📊 Enhanced PPTX Export
- **Image Verification**: Checks image accessibility before export
- **Detailed Instructions**: Step-by-step import guide for PowerPoint
- **Fallback Support**: Text descriptions when images aren't available
- **Attribution Notes**: Proper licensing information included

## How It Works

### 1. Generation Process
```
User creates presentation → AI generates slides → System identifies diagram slides → 
Searches Unsplash for relevant images → Verifies image accessibility → 
Embeds images in presentation data
```

### 2. Search Strategy
- Extracts key terms from slide titles and topics
- Searches with educational keywords (diagram, illustration, structure, process)
- Filters for landscape orientation and high-quality images
- Prioritizes educational and scientific content

### 3. Error Handling
- **API Key Missing**: Continues without images, logs warning
- **Network Issues**: Graceful timeout and fallback
- **Image Loading Fails**: Shows placeholder with fallback text
- **Rate Limiting**: Respects Unsplash API limits

## Testing the System

### With API Key
1. Set `UNSPLASH_ACCESS_KEY` in Replit Secrets
2. Create a presentation on a scientific topic (e.g., "Photosynthesis in Plants")
3. Enable "Include Diagrams" option
4. Generate presentation
5. Verify images appear in preview
6. Export to see image URLs and import instructions

### Without API Key
1. System works normally but without visual diagrams
2. Console shows informative messages about missing API key
3. Presentations include detailed text descriptions
4. Export provides instructions for manual diagram addition

## Supported Topics
- **Biology**: Cell structure, photosynthesis, DNA, anatomy, ecosystems
- **Chemistry**: Molecular structures, periodic table, chemical reactions
- **Physics**: Wave patterns, electromagnetic spectrum, atomic structure
- **Mathematics**: Geometric shapes, statistical charts, mathematical concepts
- **General Science**: Laboratory equipment, scientific processes

## Best Practices

### For Educators
1. Use specific, descriptive slide titles for better image matching
2. Include scientific terminology in slide content
3. Review generated presentations before use in classroom
4. Verify image appropriateness for your target audience

### For Administrators
1. Monitor Unsplash API usage to stay within free tier limits
2. Consider upgrading to Unsplash+ for higher usage if needed
3. Regularly check system logs for image loading issues
4. Train educators on the visual diagram features

## Troubleshooting

### Common Issues
- **No images appearing**: Check UNSPLASH_ACCESS_KEY is set correctly
- **Image loading errors**: Verify internet connectivity and API key validity
- **Rate limiting**: Wait before generating more presentations
- **Poor image matches**: Try more specific slide titles and scientific terms

### Error Messages
- `❌ UNSPLASH_ACCESS_KEY not configured`: Add API key to secrets
- `❌ Unsplash API authentication failed`: Check API key validity
- `⚠️ Diagram could not be loaded`: Network issue or image unavailable
- `❌ Image verification failed`: Image URL not accessible

## Privacy & Licensing
- All images from Unsplash are royalty-free for educational use
- Photographer attribution automatically included
- No user data sent to Unsplash (only search queries)
- Images downloaded temporarily for verification only

## Future Enhancements
- Support for additional image sources
- Custom diagram upload capability
- AI-generated educational diagrams
- Integration with institutional image libraries
- Advanced filtering by educational level

## Support
If you encounter issues with visual diagrams:
1. Check the console logs for detailed error messages
2. Verify your Unsplash API key is valid and active
3. Contact support at edu.vixenak@gmail.com for assistance
4. Include relevant error messages and slide topics in your report