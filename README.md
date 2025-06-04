# DSCPL - AI Agent #1

## 🧭 Overview

**DSCPL** is your personal spiritual assistant, guiding you daily through devotionals, prayer, meditation, and accountability. Whether you're looking to grow in faith, seek support, or simply chat, DSCPL is designed to walk with you in every season.

---

## 🌱 1. User Flow

### ✅ Step 1: Initial Selection

Upon launch, DSCPL welcomes the user with:

> *"What do you need today?"*

Users can select from:

- **Daily Devotion**
    - Watch video verses instead of reading
    - Recreate the entire Bible verse-by-verse with video content  
    - *[Inspiration Video Example](https://www.instagram.com/egypt.ontravelx/reel/DGOlYTeitul/)*
- **Daily Prayer**
- **Daily Meditation**
- **Daily Accountability**
- **Just Chat**
    - Starts a conversation with the AI agent immediately

---

### ✅ Step 2: Topic Selection

Based on the chosen category, DSCPL provides pre-defined or user-customizable topics.

#### Devotion Topics
- Dealing with Stress
- Overcoming Fear
- Conquering Depression
- Relationships
- Healing
- Purpose & Calling
- Anxiety
- Something else...

#### Prayer Topics
- Personal Growth
- Healing
- Family/Friends
- Forgiveness
- Finances
- Work/Career
- Something else...

#### Meditation Topics
- Peace
- God's Presence
- Strength
- Wisdom
- Faith
- Something else...

#### Accountability Areas
- Pornography
- Alcohol
- Drugs
- Sex
- Addiction
- Laziness
- Something else...

> 🧠 *Topics can be personalized based on user's preferences, history, and watched content.*

---

### ✅ Step 3: Weekly Overview & Goal Setting

DSCPL outlines a 7-day spiritual program:

> *"By the end of this week, you will feel more connected to God and confident in resisting temptation."*

---

### ✅ Step 4: User Confirmation

DSCPL prompts:

> *"Would you like to begin?"*

- If *yes*, it schedules daily notifications and adds reminders to the user’s Google/Apple Calendar.

---

### ✅ Step 5: Daily Program Delivery

- Sends morning notification
- Opens DSCPL with that day’s devotional content
- Syncs with the user's calendar

---

## 📖 2. Content Structure by Category

### ✝️ Devotion Format

1. **5-minute Bible Reading**  
2. **Short Prayer**  
3. **Faith Declaration**  
4. **Recommended Video** (from in-app video feed)

**Example:**

- **Scripture:** Philippians 4:6-7  
- **Prayer:** "Lord, help me release my anxieties and trust in You."  
- **Declaration:** "God is my refuge, and I will not be shaken."  
- **Video:** *Overcoming Fear with God’s Promises*

---

### 🙏 Prayer Format (ACTS Model)

1. **Adoration** – Praise God  
2. **Confession** – Repentance  
3. **Thanksgiving** – Gratitude  
4. **Supplication** – Requests  

Includes:
- **Daily Prayer Focus Prompt**  
  _E.g., Pray for someone who hurt you, or wisdom in a difficult situation_

---

### 🧘 Meditation Format

1. **Scripture Focus**  
   _E.g., Psalm 46:10 - "Be still and know that I am God."_
2. **Meditation Prompts**  
   - What does this reveal about God?
   - How can I live this out today?
3. **Breathing Guide**  
   - Inhale 4s → Hold 4s → Exhale 4s

---

### 🛡️ Accountability Format

1. **Scripture for Strength**  
2. **Truth Declarations**  
   _E.g., "I am not a slave to temptation; I am free in Christ."_
3. **Alternative Actions**  
   _Instead of [vice], try [healthy action]_
4. **SOS Feature**  
   - “I need help now!” button  
   - Immediate encouragement  
   - Scripture and action plan  
   - Contact a friend/mentor (in-app DM)

---

## 🧩 3. Technical Integration

- 🔔 **Push Notifications**: For daily spiritual engagement  
- 🎥 **Video API**: Curated faith-based content  
- 🧾 **User Input Logging**: Tracks daily and weekly progress  
- 🚨 **Emergency SOS**: For urgent accountability & emotional support  
- 📅 **Calendar Sync**: Google/Apple integration

---

## 🎛️ 4. Customization Features

- 📝 Set **custom prayer/meditation goals**  
- 📆 Choose **program length** (7, 14, 30 days)  
- ❓ Ask **questions during programs**  
- 📊 **Progress Dashboard**
    - View history of completed programs
    - Pause/resume or redo any past programs

---

**Get All Posts** (Header required*) (METHOD: GET):

   ```
   https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000
   ```

### Authorization

For autherization pass `Flic-Token` as header in the API request:

Header:

```json
"Flic-Token": "flic_b1c6b09d98e2d4884f61b9b3131dbb27a6af84788e4a25db067a22008ea9cce5"
```
---

## 📌 Final Note

DSCPL isn't just an app — it's a **companion for your spiritual journey**. Rooted in scripture, empowered by technology, and guided by grace.

---
